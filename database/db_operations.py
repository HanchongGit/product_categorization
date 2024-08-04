import sqlite3
import pandas as pd
import os
import shutil
import logging
import re

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def initialize_database(db_path):
    """Initialize the database, create tables, and set up triggers for synchronization."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create sap_model_only table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sap_model_only (
            sap_code INTEGER PRIMARY KEY,
            model_name TEXT NOT NULL
        );
    ''')

    # Create feature_db table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS feature_db (
            sap_code INTEGER PRIMARY KEY,
            model_name TEXT NOT NULL,
            feature1 TEXT,
            feature2 TEXT,
            feature3 TEXT,
            feature4 TEXT,
            feature5 TEXT,
            feature6 TEXT,
            feature7 TEXT,
            feature8 TEXT,
            feature9 TEXT,
            feature10 TEXT
        );
    ''')

    # Trigger to insert into feature_db when a new sap_code is added to sap_model_only
    cursor.execute('''
        CREATE TRIGGER IF NOT EXISTS insert_feature_after_sap
        AFTER INSERT ON sap_model_only
        BEGIN
            INSERT OR IGNORE INTO feature_db (sap_code, model_name)
            VALUES (NEW.sap_code, NEW.model_name);
        END;
    ''')

    # Trigger to insert into sap_model_only when a new sap_code is added to feature_db
    cursor.execute('''
        CREATE TRIGGER IF NOT EXISTS insert_sap_after_feature
        AFTER INSERT ON feature_db
        BEGIN
            INSERT OR IGNORE INTO sap_model_only (sap_code, model_name)
            VALUES (NEW.sap_code, NEW.model_name);
        END;
    ''')

    conn.commit()
    conn.close()

def normalize_column_names(columns):
    """Normalize column names by making them uppercase and removing punctuation and underscores."""
    return [re.sub(r'[\W_]+', '', col).upper() for col in columns]

def validate_columns(df, expected_columns, table_name):
    """Validate that the DataFrame columns match the expected columns."""
    df.columns = normalize_column_names(df.columns)
    expected_columns_normalized = normalize_column_names(expected_columns)

    if set(df.columns) != set(expected_columns_normalized) and 'SAPCODE' not in df.columns and 'MODELNAME' not in df.columns:
        missing = set(expected_columns_normalized) - set(df.columns)
        extra = set(df.columns) - set(expected_columns_normalized)
        raise ValueError(f"Table '{table_name}' column validation failed. "
                         f"Missing columns: {missing}. Extra columns: {extra}. Current columns: {df.columns}")

def validate_table_name(table_name):
    """Validate that the table name is one of the expected tables."""
    valid_tables = ['sap_model_only', 'feature_db']
    if table_name not in valid_tables:
        raise ValueError(f"Invalid table name '{table_name}'. Expected one of {valid_tables}.")

def archive_file(file_path, archive_folder):
    """Archive the file by moving it to the specified archive folder."""
    if not os.path.exists(archive_folder):
        os.makedirs(archive_folder)

    # Move the file to the archive folder
    shutil.move(file_path, os.path.join(archive_folder, os.path.basename(file_path)))

def load_data_to_table(db_path, data_folder, table_name, overwrite=False, archive_folder='archive'):
    """Load data from CSV or XLSX files into the specified table of the database."""
    validate_table_name(table_name)

    expected_columns = {
        'sap_model_only': ['sap_code', 'model_name'],
        'feature_db': ['sap_code', 'model_name', 'feature1', 'feature2', 'feature3', 'feature4', 
                       'feature5', 'feature6', 'feature7', 'feature8', 'feature9', 'feature10']
    }
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    if overwrite:
        cursor.execute(f'DROP TABLE IF EXISTS {table_name}')
        if table_name == 'sap_model_only':
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS sap_model_only (
                    sap_code INTEGER PRIMARY KEY,
                    model_name TEXT NOT NULL
                );
            ''')
        elif table_name == 'feature_db':
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS feature_db (
                    sap_code INTEGER PRIMARY KEY,
                    model_name TEXT NOT NULL,
                    feature1 TEXT,
                    feature2 TEXT,
                    feature3 TEXT,
                    feature4 TEXT,
                    feature5 TEXT,
                    feature6 TEXT,
                    feature7 TEXT,
                    feature8 TEXT,
                    feature9 TEXT,
                    feature10 TEXT
                );
            ''')

    for file in os.listdir(data_folder):
        file_path = os.path.join(data_folder, file)
        try:
            if file_path.endswith('.csv'):
                df = pd.read_csv(file_path)
            elif file_path.endswith('.xlsx'):
                df = pd.read_excel(file_path)
            else:
                continue
            
            validate_columns(df, expected_columns[table_name], table_name)

            for _, row in df.iterrows():
                if table_name == 'sap_model_only':
                    cursor.execute('''
                        INSERT OR REPLACE INTO sap_model_only (sap_code, model_name)
                        VALUES (?, ?)
                    ''', (row['SAPCODE'], row['MODELNAME']))
                
                elif table_name == 'feature_db':
                    cursor.execute('''
                        INSERT OR REPLACE INTO feature_db (sap_code, model_name, feature1, feature2, feature3,
                                                           feature4, feature5, feature6, feature7, feature8,
                                                           feature9, feature10)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ''', (row['SAPCODE'], row['MODELNAME'], row.get('FEATURE1'), row.get('FEATURE2'), 
                          row.get('FEATURE3'), row.get('FEATURE4'), row.get('FEATURE5'), row.get('FEATURE6'),
                          row.get('FEATURE7'), row.get('FEATURE8'), row.get('FEATURE9'), row.get('FEATURE10')))
            archive_file(file_path, archive_folder)
            logging.info(f"Successfully processed and archived file: {file_path}")
        
        except Exception as e:
            print(f"Error processing file {file_path}: {e}")

    conn.commit()
    conn.close()

def load_data_from_sql_table(db_path='database/product_features.db'):
    """
    Load product data from the 'feature_db' table.

    Args:
        db_path (str): Path to the SQLite database file.

    Returns:
        list of dict: A list of product data dictionaries from the 'feature_db' table.
    """
    table_name = 'feature_db'  # Always load from 'feature_db'
    
    try:
        logging.info(f"Loading data from SQL table: {table_name}")

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute(f'SELECT * FROM {table_name}')
        columns = [column[0] for column in cursor.description]
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]

        logging.info(f"Successfully loaded {len(data)} records from table: {table_name}")
        
        conn.close()
        return data
    
    except sqlite3.Error as e:
        logging.error(f"Error loading data from SQL table {table_name}: {e}")
        return []






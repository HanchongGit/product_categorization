import os
from .db_operations import (
    initialize_database,
    load_data_to_table,
    load_data_from_sql_table
)

# Expose the public API of the package
__all__ = [
    'initialize_database',
    'load_data_to_table',
    'load_data_from_sql_table'
]

DATA_FOLDER = 'database/excel_data_files'
if not os.path.exists(DATA_FOLDER):
    os.makedirs(DATA_FOLDER)
ARCHIVE_FOLDER = 'archive'
DB_PATH = 'database/product_features.db'

def automatically_load_data():
    """Automatically load data from available CSV or XLSX files in the data folder."""
    if not os.path.exists(DB_PATH):
        initialize_database(DB_PATH)
        print(f"Initialized database at {DB_PATH}.")
    
    if any(file.endswith(('.csv', '.xlsx')) for file in os.listdir(DATA_FOLDER)):
        try:
            load_data_to_table(DB_PATH, DATA_FOLDER, 'feature_db', archive_folder=ARCHIVE_FOLDER)
            print(f"Data loaded successfully from {DATA_FOLDER} and archived in {ARCHIVE_FOLDER}.")
        except Exception as e:
            print(f"Error loading data automatically: {e}")
    else:
        print(f"No CSV or XLSX files found in {DATA_FOLDER} to load.")

# Automatically load data if any files are present
automatically_load_data()
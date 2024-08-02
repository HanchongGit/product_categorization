import csv
import os
import pandas as pd
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_data_from_csv_folder(folder_path):
    """
    Load product data from all CSV files in a folder.

    Args:
        folder_path (str): Path to the folder containing CSV files.

    Returns:
        list of dict: A combined list of product data dictionaries from all CSV files.
    """
    all_data = []
    try:
        logging.info(f"Loading data from CSV files in folder: {folder_path}")
        
        for file_name in os.listdir(folder_path):
            if file_name.endswith('.csv'):
                file_path = os.path.join(folder_path, file_name)
                with open(file_path, mode='r', newline='', encoding='utf-8') as file:
                    reader = csv.DictReader(file)
                    data = [row for row in reader]
                
                if validate_data(data):
                    all_data.extend(data)
                else:
                    logging.warning(f"Data validation failed for CSV file: {file_path}")

        logging.info(f"Successfully loaded {len(all_data)} records from CSV files.")
    except FileNotFoundError:
        logging.error(f"Folder not found: {folder_path}")
    except Exception as e:
        logging.error(f"Error loading CSV files from folder {folder_path}: {e}")

    return all_data

def load_data_from_excel_folder(folder_path):
    """
    Load product data from all Excel files in a folder.

    Args:
        folder_path (str): Path to the folder containing Excel files.

    Returns:
        list of dict: A combined list of product data dictionaries from all Excel files.
    """
    all_data = []
    try:
        logging.info(f"Loading data from Excel files in folder: {folder_path}")
        
        for file_name in os.listdir(folder_path):
            if file_name.endswith('.xlsx'):
                file_path = os.path.join(folder_path, file_name)
                data_frame = pd.read_excel(file_path)
                data = data_frame.to_dict(orient='records')
                
                if validate_data(data):
                    all_data.extend(data)
                else:
                    logging.warning(f"Data validation failed for Excel file: {file_path}")

        logging.info(f"Successfully loaded {len(all_data)} records from Excel files.")
    except FileNotFoundError:
        logging.error(f"Folder not found: {folder_path}")
    except Exception as e:
        logging.error(f"Error loading Excel files from folder {folder_path}: {e}")

    return all_data

def validate_data(data):
    """
    Validate product data to ensure it has the necessary fields.

    Args:
        data (list of dict): Product data to validate.

    Returns:
        bool: True if data is valid, False otherwise.
    """
    required_fields = {'SAP Code', 'Model Name'}
    for record in data:
        if not required_fields.issubset(record.keys()):
            logging.error(f"Missing required fields in record: {record}")
            return False
    return True

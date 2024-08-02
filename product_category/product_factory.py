from .base_product import Product
from .analog_camera import Analog_Camera
from .generic_product import Generic_Product
from database import load_data_from_csv_folder, load_data_from_excel_folder

# Global flag to track if the database is loaded
database_loaded = False

def load_product_database():
    """
    Load the product database into memory if not already loaded.
    """
    global database_loaded
    if not database_loaded:
        # Load data from all files in the directory
        csv_data = load_data_from_csv_folder('database/data_files')
        excel_data = load_data_from_excel_folder('database/data_files')

        for row in csv_data + excel_data:  # Combine data from both sources
            sap_code = str(row.get('SAP Code', '')).strip()
            model_name = str(row.get('Model Name', '')).strip()
            if sap_code and model_name:
                Product.product_data_by_sap[sap_code] = model_name
                Product.product_data_by_model[model_name] = sap_code

        database_loaded = True

def create_product(sap_code, model_name):
    """
    Factory function to create a product instance based on criteria.
    """
    # Ensure the database is loaded before creating a product
    load_product_database()

    # Check criteria for Analog_Camera
    if model_name.startswith('DS-2C') or model_name.startswith('HWT-') or model_name.startswith('THC-'):
        return Analog_Camera(sap_code, model_name)

    # Add additional criteria here for other subclasses
    # Example: 
    # elif model_name.startswith('XYZ'):
    #     return SpecificProductSubclass(sap_code, model_name)

    # Default to Generic_Product if no specific subclass criteria are met
    # return Other_Product(sap_code, model_name)
from .base_product import Product
from .analog_camera import Analog_Camera
from .generic_product import Generic_Product

def create_product(sap_code, model_name):
    """
    Factory function to create a product instance based on criteria.
    """
    
    product = Product(sap_code, model_name)

    # Check criteria for Analog_Camera
    if product.model_name.startswith('DS-2C') or product.model_name.startswith('HWT-') or product.model_name.startswith('THC-'):
        return Analog_Camera(sap_code, model_name)

    # Add additional criteria here for other subclasses
    # Example: 
    # elif model_name.startswith('XYZ'):
    #     return SpecificProductSubclass(sap_code, model_name)

    # Default to Generic_Product if no specific subclass criteria are met
    return product
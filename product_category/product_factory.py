from .base_product import Product
from .analog_camera import Analog_Camera
from .non_video import NonVideo
from .generic_product import Generic_Product

def create_product(sap_code, model_name):
    """
    Factory function to create a product instance based on criteria.
    """
    
    product = Product(sap_code, model_name)

    # Check criteria for Analog_Camera
    if product.class_name == 'Analog Camera' or product._matches_any(['*DS-2C*', '*HWT-*', '*THC-*']):
        return Analog_Camera(sap_code, model_name)
    
    if product.class_name == 'Non-Video' or product.brandline == 'Pyronix' or product._matches_any(["*DS-K*", "*IC S50*", "*ISD-S*", "*NP-S*", "*DS-PEA*", "*DS-P*"]):
        return NonVideo(sap_code, model_name)

    # Add additional criteria here for other subclasses
    # Example: 
    # elif model_name.startswith('XYZ'):
    #     return SpecificProductSubclass(sap_code, model_name)

    # Default to Generic_Product if no specific subclass criteria are met
    return product
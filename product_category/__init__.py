from .base_product import Product
from .analog_camera import Analog_Camera
from .generic_product import Generic_Product
from .product_factory import create_product

# Define what is accessible from the package
__all__ = ['Product', 'Analog_Camera', 'Generic_Product', 'create_product']
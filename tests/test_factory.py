import pytest
from product_category.product_factory import create_product
from product_category.analog_camera import Analog_Camera
from product_category.generic_product import Generic_Product

def test_create_analog_camera():
    product = create_product('102202581', 'DS-2CE16D8T-IT3(3.6mm)(O-STD)')
    assert isinstance(product, Analog_Camera)

# def test_create_generic_product():
#     product = create_product('123456789', 'XYZ-Model')
#     assert isinstance(product, Generic_Product)

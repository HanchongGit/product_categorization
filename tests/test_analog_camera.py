import pytest
from product_category.analog_camera import Analog_Camera

def test_hikvision_features():
    product = Analog_Camera('300508317', 'DS-2CE16D8T-IT3(3.6mm)(O-STD)')
    assert product.brandline == 'Hikvision'
    assert product.feature1 == '2 MP'
    assert product.feature2 == 'D8T'
    assert product.feature3 == 'Pro'
    assert product.feature4 == 'No SHL'
    assert product.feature5 == 'Fixed Lens'
    assert product.feature6 == 'No POC'

def test_hiwatch_features():
    product = Analog_Camera(None, 'HWT-T129-M(3.6mm)(HIK SPAIN)')
    assert product.brandline == 'HiWatch'
    assert product.feature1 == '2 MP'
    assert product.feature2 == 'ColorVu'
    assert product.feature3 == 'IR Light'
    assert product.feature4 == 'Fixed Lens'
    assert product.feature5 == None
    assert product.feature6 == None

def test_hilook_features():
    product = Analog_Camera(None, 'THC-T323-Z(2.7-13.5mm)(HiLook STD)')
    assert product.brandline == 'HiLook'
    assert product.feature1 == '2 MP'
    assert product.feature2 == 'Basic'
    assert product.feature3 == 'IR Light'
    assert product.feature4 == 'Vari-Focal'
    assert product.feature5 == None
    assert product.feature6 == None


import pytest
from product_category.non_video import NonVideo

def test_ACS_features():
    product = NonVideo('302900516',	'DS-K1104M(O-STD)')
    assert product.feature1 == 'ACS'
    assert product.feature2 == 'Card Reader'
    assert product.feature3 == 'others'
    assert product.feature4 == 'others'
    assert product.feature5 == 'others'
    assert product.feature6 == 'STD'

def test_intercom_features():
    product = NonVideo('305301408',	'DS-KH6320-TE1(O-STD)')
    assert product.feature1 == 'Intercom'
    assert product.feature2 == 'Indoor Station'
    assert product.feature3 == 'Pro Indoor Station'
    assert product.feature4 == 'others'
    assert product.feature5 == 'others'
    assert product.feature6 == 'STD'

def test_pyronix_features():
    product = NonVideo(None, 'FPV2TELDE')
    assert product.brandline == 'Pyronix'
    assert product.feature1 == 'PYRONIX'
    assert product.feature2 == None
    assert product.feature3 == None
    assert product.feature4 == None
    assert product.feature5 == None
    assert product.feature6 == None

def test_alarm_features():
    product = NonVideo('302401665', None)
    assert product.feature1 == 'Alarm'
    assert product.feature2 == 'AX PRO'
    assert product.feature3 == 'Wireless Accessory'
    assert product.feature4 == None
    assert product.feature5 == None
    assert product.feature6 == None
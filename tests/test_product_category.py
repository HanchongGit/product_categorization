import pytest
from product_category.base_product import Product

@pytest.fixture
def setup_product_data():
    # Set up test data for the base Product class
    Product.product_data_by_sap = {
        '102202581': 'DS-2CE16D8T-IT3(3.6mm)(O-STD)',
        '202002308': 'K3G501-C'
    }
    Product.product_data_by_model = {
        'DS-2CE16D8T-IT3(3.6mm)(O-STD)': '102202581',
        'K3G501-C': '202002308'
    }

def test_lookup_by_sap_code(setup_product_data):
    product = Product('102202581', None)
    assert product.model_name == 'DS-2CE16D8T-IT3(3.6mm)(O-STD)'

def test_lookup_by_model_name(setup_product_data):
    product = Product(None, 'K3G501-C')
    assert product.sap_code == '202002308'

def test_no_identifiers_raises_error():
    with pytest.raises(ValueError):
        Product(None, None)

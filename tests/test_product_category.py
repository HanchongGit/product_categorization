import pytest
from product_category.base_product import Product

def test_lookup_by_sap_code():
    product = Product('102202581', None)
    assert product.model_name == 'IT-AF15G10DS-640X17S1'

def test_lookup_by_model_name():
    product = Product(None, 'K3G501-C')
    assert product.sap_code == '202002308'

def test_no_identifiers_raises_error():
    with pytest.raises(ValueError):
        Product(None, None)

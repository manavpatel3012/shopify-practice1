import pytest
from src.cart import Product

def test_product_created_successfully():
    product = Product("Laptop", 999.99, "P001", 10)
    assert product.name == "Laptop"
    assert product.price == 999.99
    assert product.product_id == "P001"
    assert product.stock == 10

def test_empty_productName():
    with pytest.raises(ValueError):
        Product("", 999.99, "P002", 5)

def test_product_rejects_empty_price():
    with pytest.raises(ValueError):
        Product("P002", "", 999.9, 5)
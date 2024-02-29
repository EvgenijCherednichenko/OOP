import pytest
from src.product import Product


@pytest.fixture
def product():
    return Product('Капуста', 'Белокачанная с привкусом USA', 67.5, 5)


def test_init(product):
    assert product.name == 'Капуста'
    assert product.description == 'Белокачанная с привкусом USA'
    assert product.price == 67.5
    assert product.total_in_stock == 5

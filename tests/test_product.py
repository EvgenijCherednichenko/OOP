import pytest
from src.product import Product


@pytest.fixture
def product():
    return Product('Samsung Galaxy C23 Ultra',
                   '256GB, Серый цвет, 200MP камера',
                   180000.0,
                   5)


def test_init(product):
    assert product.name == 'Samsung Galaxy C23 Ultra'
    assert product.description == '256GB, Серый цвет, 200MP камера'
    assert product.price == 180000.0
    assert product.quantity == 5

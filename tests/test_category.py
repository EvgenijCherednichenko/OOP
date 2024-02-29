import pytest
from src.category import Category


@pytest.fixture
def category_product():
    return Category('Овощи', 'Из местных плантаций', ['лук', 'картофель', 'морковь', 'капуста'])


def test_init(category_product):
    assert category_product.name == 'Овощи'
    assert category_product.description == 'Из местных плантаций'
    assert category_product.goods == ['лук', 'картофель', 'морковь', 'капуста']
    assert category_product.total_categories == 1
    assert category_product.total_products == 4

import pytest
from src.category import Category


@pytest.fixture
def category_product():
    return Category('Смартфоны',
                    'Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни',
                    ['Samsung Galaxy C23 Ultra', '256GB, Серый цвет, 200MP камера', '180000.0', '5'])


def test_init(category_product):
    assert category_product.name == 'Смартфоны'
    assert category_product.description == 'Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни'
    assert category_product.products == ['Samsung Galaxy C23 Ultra', '256GB, Серый цвет', '180000.0', '5']
    assert category_product.total_categories == 1
    assert category_product.total_products == 4

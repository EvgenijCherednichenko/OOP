class Category:
    """Категории тавара"""
    name: str         # название товара
    description: str  # описание товара
    goods: list       # товары в этой категории

    total_categories = 0
    total_products = 0

    def __init__(self, name, description, goods):
        self.name = name
        self.description = description
        self.goods = goods

        Category.total_categories += 1
        Category.total_products += len(self.goods)


print(Category.total_categories)
print(Category.total_products)

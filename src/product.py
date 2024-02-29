class Product:
    """Товар"""
    name: str            # название товара
    description: str     # описание товара
    price: float         # цена товара
    total_in_stock: int  # всего в наличии

    def __init__(self, name, description, price, total_in_stock):
        self.name = name
        self.description = description
        self.price = price
        self.total_in_stock = total_in_stock

class Category:
    """Категории тавара"""
    name: str         # название товара
    description: str  # описание товара
    products: list  # список товаров в этой категории

    total_categories = 0
    total_products = 0

    def __init__(self, name, description, __products):
        """Создаем шаблон класса 'Категории товара' """
        self.name = name
        self.description = description
        self.__products = __products

        Category.total_categories += 1
        Category.total_products += len(self.__products)

    def add_goods(self, good):
        """Принимает на вход обьект товара и добавляет его в список"""
        self.__products.append(good)

    @property
    def products(self):
        """геттер, который выводит список товаров"""
        prod = ''
        for good in self.__products:
            prod += f'{good.name}, {good.price} руб. Остаток: {good.quantity} шт.\n'
        return prod

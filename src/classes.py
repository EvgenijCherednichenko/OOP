from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """ Абстрактный базовый класс"""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Category:
    """Класс категории тавара"""
    name: str  # название категории
    description: str  # описание категории
    products: list  # список товаров в этой категории

    total_categories = 0
    total_products = 0

    def __init__(self, name, description, products):
        """Создаем шаблон класса 'Категории товара' """
        self.name = name
        self.description = description
        self.__products = products

        Category.total_categories += 1
        Category.total_products += len(self.__products)

    def __str__(self):
        """Выводит информацию для пользователя"""
        return f'{self.name}, количество продуктов: {len(self.__products)} шт.'

    def __len__(self):
        """Суммирует колличество продуктов"""
        return len(self.__products)

    def add_goods(self, good):
        """Принимает на вход обьект товара и добавляет его в список"""
        Category.total_products += good.quantity

        if not issubclass(good.__class__, (SmartPhones, LawnGrass)):
            raise TypeError('Продукт не соответсвует классу')
        self.__products.append(good)

    @property
    def display(self):
        """Данный метод позволяет принтом вывести приватный список товаров"""
        return self.__products

    @property
    def counting_goods(self):
        return len(self.__products)

    def __repr__(self):
        return f'{self.name}, {self.description}, {self.__products}'

    @property
    def products(self):
        """геттер, который выводит список товаров"""
        prod = ''
        for good in self.__products:
            prod += f'{good.name}, {good.price} руб. Остаток: {good.quantity} шт.\n'
        return prod

    def average_sum(self):
        """Метод, который подсчитывает средний ценник всех товаров.
        Если в Категории не передан ни один товар, возвращает 0"""
        try:
            total_sum = 0
            for good in self.__products:
                total_sum += good.price
            average_sum = total_sum / len(self.__products)
            return average_sum
        except ZeroDivisionError:
            return 0


class ZeroQuantity(Exception):
    """
    Класс исключения, когда в «Категорию»
    добавляется товар с нулевым количеством
    """

    def __init__(self, message="Ошибка количества"):
        self.message = message
        super().__init__(message)


class MixinRepr:
    """ Миксин, который можно добавить к каждому классу
        для вывода информации в консоль о том, что был создан объект.
    """

    def __init__(self, *args, **kwargs):
        print(repr(self))

    def __repr__(self):
        return f"{self.__class__.__name__} ({self.__dict__.items()})"


class Product(BaseProduct, MixinRepr):
    """Товар"""
    name: str  # название товара
    description: str  # описание товара
    price: float  # цена товара
    quantity: int  # всего в наличии
    count_product = 0  # Счетчик количества продуктов (экземпляров, не остатка)

    def __init__(self, name, description, price, quantity):
        """Инициализация продуктов"""
        super().__init__()
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

        Product.count_product += 1  # при создании экземлпяра, счетчик увеличивается на 1

    def __str__(self):
        """Выводит информацию для пользователя"""
        return f'{self.name}, {self.__price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        """Выводит общую сумму"""
        return (self.price * self.quantity) + (other.price * other.quantity)

    @classmethod
    def create_products(cls, new_prod):
        """Добавляет новые товары"""
        name, price, description, quantity = new_prod.split(',')
        return cls(name, price, description, quantity)

    @property
    def price(self):
        """Задаёт цену"""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Выводит сообщение, при некорректной цены"""
        float(new_price)
        if new_price <= 0.0:
            print('Цена введена не корректно!')
        elif new_price < self.__price:
            answer = input('Цена ниже преждней. Вы хотите изменить цену (y/n):\n').lower()
            if answer == 'y':
                self.__price = new_price
        else:
            self.__price = new_price

    def __repr__(self):
        super().__repr__()


class SmartPhones(Product, MixinRepr):
    """Класс SmartPhones(Смартфон) наследник от Product"""
    capacity: float  # роизводтельность "Гц"
    model: str  # модель
    memory: int  # объем встроенной памяти
    color: str  # цвет

    def __init__(self, name, description, price, quantity, capacity, model, memory, color):
        """supper().__init__ от SmartPhones"""
        super().__init__(name, description, price, quantity)
        self.capacity = capacity
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        """Суммирование объектов, в случае, если объект другого класса - вывод ValueError"""
        if isinstance(other, SmartPhones):
            return (self.price * self.quantity) + (other.price * other.quantity)
        raise ValueError("Ошибка")

    def __repr__(self):
        super().__repr__()


class LawnGrass(Product, MixinRepr):
    """Класс LawnGrass(Трава газонная) наследник от Product"""
    country: str  # страна-производитель
    period: int  # срок прорастания
    color: str  # цвет

    def __init__(self, name, description, price, quantity, country, period, color):
        """supper().__init__ от LawnGrass"""
        super().__init__(name, description, price, quantity)
        self.country = country
        self.period = period
        self.color = color

    def __add__(self, other):
        """Суммирование объектов, в случае, если объект другого класса - вывод ValueError"""
        if not isinstance(other, LawnGrass):
            raise ValueError("Ошибка")
        return (self.price * self.quantity) + (other.price * other.quantity)

    def __repr__(self):
        super().__repr__()


def printing():
    """Метод проверки корректности методов классов"""

    category_1 = Category('Телефоны', 'мобильные телефоны', 'products')  # Экземпляр класса Category

    phone_1 = SmartPhones('LG', 'smartphone', 20732, 3, 1120.00, 'V50',
                          512, 'Black')
    phone_2 = SmartPhones('Motorola', 'Раскладушка', 2823.50, 3, 516, 'V3',
                          8, 'Black')

    category_1.add_goods(phone_1)
    category_1.add_goods(phone_2)

    try:
        category_2 = Category('Газонная трава', 'трава для сада', 'products')
        grass_1 = LawnGrass('Премиум-газон', 'Премиум', 1000, 0, 'Россия',
                            13, 'green')
        category_2.add_goods(grass_1)
    except ZeroQuantity:
        print("Добавляется товар с нулевым количеством")
    else:
        print("Товар добавлен")
    finally:
        print("Обработка добавления товара завершена")

    # print(f'Общая сумма категории "Смартфон": {phone_1 + phone_2}')
    #
    # grass_1 = LawnGrass('Премиум-газон', 'Премиум', 1000, 3, 'Россия',
    #                     13, 'green')
    # grass_2 = LawnGrass('Газон дачный', 'Эконом', 200, 10, 'Россия',
    #                     10, 'light-green')
    # print(f'Общая сумма категории "Трава газонна": {grass_1 + grass_2}')
    #
    # # category_1.add_goods(phone_2)  # Проверка, что обновленный метод append_goods работает корректно
    #
    # print(grass_1)  # Вывод на печать категории, с добавленным новым продуктом


if __name__ == '__main__':
    printing()

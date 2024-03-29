class Product:
    """Товар"""
    name: str  # название товара
    description: str  # описание товара
    price: float  # цена товара
    quantity: int  # всего в наличии
    count_product = 0  # Счетчик количества продуктов (экземпляров, не остатка)

    def __init__(self, name, description, price, quantity):
        """Инициализация продуктов"""
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


class SmartPhones(Product):
    """Класс SmartPhones наследник от Product"""
    capacity: float  # роизводтельность "Гц"
    model: str       # модель
    memory: int      # объем встроенной памяти
    color: str       # цвет

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


class LawnGrass(Product):
    """Класс LawnGrass наследник от Product"""
    country: str  # страна-производитель
    period: int   # срок прорастания
    color: str    # цвет

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

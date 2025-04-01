# Лабораторная по ООП №3
## Практическая работа 
### Задание 1

Создайте класс Roman (Римское Число), представляющий римское число
и поддерживающий операции +, -, *, /.
Совет
При реализации класса следуйте рекомендациям:
•
операции +, -, *, / реализуйте как специальные методы (＿add＿ и др.);
методы преобразования имеет смысл реализовать как статические
методы, позволяя не создавать экземпляр объекта в случае, если
необходимо выполнить только преобразования чисел.
При выполнении задания необходимо построить UML-диаграмма
классов приложения

#### Решение

~~~python
class Roman:
    def __init__(self, number: int):
        self.__roman: RomanNumber = RomanNumber(number)
    """
    Класс, представляющий из себя набор функций для работы с римскими числами
    Реализует в себе методы для преобразования чисел, и работы с ними
    """
    

    @staticmethod 
    def _reform(number: int):
        roman: str = {
            "M": 1000,
            "CM": 900,
            "D": 500,
            "XD": 400,
            "C": 100,
            "XC": 90,
            "L": 50,
            "XL": 40,
            "X": 10,
            "IX": 9,
            "V": 5,
            "IV": 4,
            "I": 1
        }
        elem: str = ""
        for key, value in roman.items():
            while(True):
                if(number >= value):
                    elem += key
                    number -= value
                else:
                    break
        return elem
    """
    Метод, который преобразует любое число в римское. Возвращает строку с римскими цифрами 
    """

    @staticmethod 
    def prereform(number: str):
        roman: str = {
            "M": 1000,
            "CM": 900,
            "D": 500,
            "XD": 400,
            "C": 100,
            "XC": 90,
            "L": 50,
            "XL": 40,
            "X": 10,
            "IX": 9,
            "V": 5,
            "IV": 4,
            "I": 1
        }
        elem: int = 0
        str_num = number.get_number()
        for key, value in roman.items():
            for i in range(0, len(str_num)):
                if(i >= len(str_num) - 1):
                    if (roman[str_num[i]] > roman[str_num[i - 1]]):
                        break
                    if(str_num[i] == key):
                        elem += value
                    break
                if (roman[str_num[i]] < roman[str_num[i + 1]]):
                    sum = str_num[i] + str_num[i+1]
                    if(sum == key):
                        elem += value
                elif (str_num[i] == key):
                    if(i >= 1):
                        if (roman[str_num[i]] > roman[str_num[i - 1]]):
                            break
                    elem += value
        return elem
    
    """
    Метод для преобразования римский чисел в обычное представление. Возвращает целочисленное число
    """

    def get_number(self):
        return self.__roman.get_intNumber()
    
    """
    Позволяет получить число, преображенное в римское
    """
    
    def __add__(self, other):
        return RomanNumber(self.__roman.get_intNumber() + other.__roman.get_intNumber())
    """
    Метод суммы двух римских чисел, возвращает число обычного представления
    """

    def __sub__(self, other):
        return RomanNumber(self.__roman.get_intNumber() + other.__roman.get_intNumber())
    """
    Метод разности двух римских чисел, возвращает число обычного представления
    """

    def __mul__(self, other):
        return RomanNumber(self.__roman.get_intNumber() + other.__roman.get_intNumber())
    """
    Метод перемножения двух римских чисел, возвращает число обычного представления
    """

    def __floordiv__(self, other):
        return RomanNumber(self.__roman.get_intNumber() + other.__roman.get_intNumber())
    """
    Метод деления двух римских чисел, возвращает число обычного представления
    """
    
    def __str__(self):
        return self.__roman
    """
    Метод вывод всех представлений числа
    """
    
class RomanNumber():
    def __init__(self, intNumber: int):
        self.__intNumber: int = intNumber
        self.__rimNumber: str = Roman._reform(intNumber)
    """
    Класс, представляющий собой римское число и его обычный аналог. Наследуется от класса Roman
    """

    def get_intNumber(self):
        return self.__intNumber
    """
    Метод для получения целочисленного представления числа
    """
    
    def get_rimNumber(self):
        return self.__rimNumber
    """
    Метод для получения римского числа
    """

    def __str__(self):
        return str(self.__intNumber) + " - " + self.__rimNumber
    """
    Метод вывода строкового формата двух представлений числа
    """
~~~

### Задание 2

Пиццерия предлагает клиентам три вида пиццы: Пепперони, Барбекю и Дары Моря, 
каждая из которых определяется тестом, соусом и начинкой.
Требуется спроектировать и реализовать приложение для терминала,
позволяющее обеспечить обслуживание посетителей.
Дополнительная информация
В бизнес-процессе работы пиццерии в контексте задачи можно выделить
3 сущности (объекта):
•Терминал: отвечает за взаимодействие с пользователем:
o вывод меню на экран;
o прием команд от пользователя (выбор пиццы, подтверждение
заказа, оплата и др.);
Заказ: содержит список заказанных пицц, умеет подсчитывать свою
стоимость;
Пицца: содержит заявленные характеристики пиццы, а также умеет себя
подготовить (замесить тесто, собрать ингредиенты и т.д.), испечь,
порезать и упаковать.
Т.к. пиццерия реализует несколько видов пиццы, которые различаются
характеристиками, логично будет сделать общий класс Пицца, а в дочерних
классах (например, классе ПиццаБарбекю) уточнить характеристики
конкретной пиццы.
Диаграмма указанных классов в нотации UML приведена на Рисунке 1.

#### Решение

#### main.py
~~~python
from terminal import *

# Пример использования терминала
terminal = Terminal()

# Отображаем меню
terminal.show_menu()

# Обрабатываем команды (добавляем пиццы в заказ)
terminal.add_pizza_to_order(1)  # Добавляем Pepperoni
terminal.add_pizza_to_order(3)  # Добавляем Seafood

# Принимаем оплату и завершаем заказ
terminal.finalize_order()
~~~

#### order.py
~~~python
class Order:
    """ Класс Order хранит заказанные пиццы и их количество. """
    
    def __init__(self):
        self.__pizzas = []
    
    def __str__(self):
        return f"Заказ: {[pizza.name for pizza in self.__pizzas]}, Количество: {len(self.__pizzas)}"
    
    def add_pizza(self, pizza):
        """ Добавляет пиццу в заказ. """
        self.__pizzas.append(pizza)
    
    def total_price(self):
        """ Подсчитывает общую сумму заказа. """
        return sum(pizza.price for pizza in self.__pizzas)
    
    def execute(self):
        """ Выполняет заказ: готовит, выпекает, режет и упаковывает пиццы. """
        for pizza in self.__pizzas:
            pizza.prepare()
            pizza.bake()
            pizza.cut()
            pizza.box()
        print(f"Заказ выполнен! Общая стоимость: {self.total_price()}₽")
        self.__pizzas.clear()
~~~

#### pizza.py
~~~python
class Pizza:
    """
    Класс Pizza описывает пиццу с ее основными характеристиками:
    название, тип теста, соус, начинка и стоимость.
    """
    
    def __init__(self, name, dough, sauce, filling, price):
        self.__name = name
        self.__dough = dough
        self.__sauce = sauce
        self.__filling = filling
        self.__price = price
    
    def __str__(self):
        return (f"Пицца: {self.name}, Тесто: {self.dough}, Соус: {self.sauce}, "
                f"Начинка: {', '.join(self.filling)}, Цена: {self.price}₽")
    
    @property
    def name(self): return self.__name
    @name.setter
    def name(self, value): self.__name = value
    
    @property
    def dough(self): return self.__dough
    @dough.setter
    def dough(self, value): self.__dough = value
    
    @property
    def sauce(self): return self.__sauce
    @sauce.setter
    def sauce(self, value): self.__sauce = value
    
    @property
    def filling(self): return self.__filling
    @filling.setter
    def filling(self, value): self.__filling = value
    
    @property
    def price(self): return self.__price
    @price.setter
    def price(self, value): self.__price = value
    
    def prepare(self): print(f"Готовим {self.name}...")
    def bake(self): print(f"Выпекаем {self.name}...")
    def cut(self): print(f"Режем {self.name} на кусочки...")
    def box(self): print(f"Упаковываем {self.name}...")
    

class PizzaPepperoni(Pizza):
    """ Пицца Пепперони """
    def __init__(self):
        super().__init__("Пепперони", "Тонкое тесто", "Томатный соус", ["Пепперони", "Сыр"], 300)


class PizzaBarbecue(Pizza):
    """ Пицца Барбекю """
    def __init__(self):
        super().__init__("Барбекю", "Толстое тесто", "Соус барбекю", ["Курица", "Лук", "Соус барбекю"], 350)


class PizzaSeafood(Pizza):
    """ Пицца с морепродуктами """
    def __init__(self):
        super().__init__("Морепродукты", "Тонкое тесто", "Белый соус", ["Креветки", "Кальмары", "Мидии"], 450)

~~~

#### terminal.py
~~~python
from pizza import *
from order import *

class Terminal:
    """ Терминал для оформления заказа. """
    
    def __init__(self):
        self.__menu = [PizzaPepperoni(), PizzaBarbecue(), PizzaSeafood()]
        self.__current_order = Order()
    
    def show_menu(self):
        """ Отображает доступные пиццы. """
        print("Меню пицц:")
        for idx, pizza in enumerate(self.__menu, 1):
            print(f"{idx}. {pizza.name} - {pizza.price}₽")
    
    def add_pizza_to_order(self, choice):
        """ Добавляет выбранную пиццу в заказ. """
        if 1 <= choice <= len(self.__menu):
            self.__current_order.add_pizza(self.__menu[choice - 1])
            print(f"Добавлена {self.__menu[choice - 1].name}.")
        else:
            print("Ошибка выбора!")
    
    def finalize_order(self):
        """ Принимает оплату и завершает заказ. """
        print(f"К оплате: {self.__current_order.total_price()}₽")
        print("Оплата принята.")
        self.__current_order.execute()
~~~
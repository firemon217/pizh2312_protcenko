# Лабораторная по ООП №5
## Практическая работа 
### Задание 1

Создайте класс-контейнер, который будет содержать набор объектов из
предыдущей задачи. Например, класс Vector Collection будет содержать
объекты класса Vector.
Для класса-контейнера предусмотрите:
специальные методы:
init(self, …) - инициализация с необходимыми параметрами;
str＿ (self) - представление объекта в удобном для человека
виде;
ogetitem () - индексация и срез для класса-контейнера.
поля, методы, свойства:
o поле _data - содержит набор данных;
o метод add(self, value) - добавляет элемент value в контейнер;
o метод remove(self, index) - удаляет элемент из контейнера по
индексу index;
o метод save(self, filename) - сохраняет объект в JSON-
файл filename;
o метод load(self, filename) - загружает объект из JSON-
файла filename.
При выполнении задания необходимо построить UML-диаграмму
классов приложения

#### Решение

#### fraction
~~~python
import json

class Fraction:
    """Класс, реализующий дробное число, методы его воспроизведения и математические операции с ними"""
    def __init__(self, number: str):
        self.__number: str = number
        self.__floatNumber: float = self.from_string(number)

    @property
    def number(self): return self.__number

    @number.setter
    def number(self, value: str): 
        self.__number = value
        self.__floatNumber = self.from_string(value)

    def from_string(self, number: str) -> float:
        """Метод, переводящий строковое представление дробного числа в числовое"""
        return self.get_numerator(number)/ self.get_denominator(number)
    
    def get_denominator(self, number: str) -> int:
        """Метод, возвращающий знаменатель числа"""
        denominator: int = int(number.split("/")[1])
        return denominator

    def get_numerator(self, number: str) -> int:
        """Метод, возвращающий числитель числа"""
        numerator: int = int(number.split("/")[0])
        return  int(numerator)
    
    def reduce(self, number: str) -> str:
        """Метод, сокращающий число"""
        denominator = self.get_denominator(number)
        numerator = self.get_numerator(number)
        for i in range(1, numerator):
            if(numerator < i):
                break
            if (numerator % i == 0 and denominator % i == 0):
                numerator /= i
                denominator /= i
        return f"{int(numerator)} / {int(denominator)}"
    
    def __str__(self):
        """Метод, возвращающий строковое представление числа"""
        return str(self.__floatNumber) + " - " + self.__number
    
    def __add__(self, other):
        """Метод, реализующий сложение дробных чисел"""
        denominator:int = self.get_denominator(self.__number) * other.get_denominator(other.__number)
        numerator:int = self.get_numerator(self.__number) * other.get_denominator(other.__number) + other.get_numerator(other.__number) * self.get_denominator(self.__number)
        number: str = self.reduce(f"{int(numerator)} / {int(denominator)}")
        return Fraction(number)
    
    def __sub__(self, other):
        """Метод, реализующий вычитание дробных чисел"""
        denominator:int = self.get_denominator(self.__number) * other.get_denominator(other.__number)
        numerator:int = self.get_numerator(self.__number) * other.get_denominator(other.__number) - other.get_numerator(other.__number) * self.get_denominator(self.__number)
        number: str = self.reduce(f"{int(numerator)} / {int(denominator)}")
        return Fraction(number)
    
    def __mul__(self, other):
        """Метод, реализующий перемножение дробных чисел"""
        denominator:int = self.get_denominator(self.__number) * other.get_denominator(other.__number)
        numerator:int = self.get_numerator(self.__number) * other.get_numerator(other.__number)
        number: str = self.reduce(f"{int(numerator)} / {int(denominator)}")
        return Fraction(number)
    
    def __floordiv__(self, other):
        """Метод, реализующий деление дробных чисел"""
        denominator:int = self.get_denominator(self.__number) * other.get_numerator(other.__number)
        numerator:int = self.get_numerator(self.__number) * other.get_denominator(other.__number)
        number: str = self.reduce(f"{int(numerator)} / {int(denominator)}")
        return Fraction(number)
    
    def save(self, filename: str):
        """Метод, реализующий сохранение объекта числа в файл"""
        f = open(filename+".json", "w")
        f.write(f'{{\n"number": "{self.__number}",\n"float_number": "{self.__floatNumber}"\n}}')
        f.close()

    def load(self, filename):
        """Метод, реализующий выгрузку объекта числа из файла"""
        f = open(filename+".json", "r")
        dic = json.loads(f.read())
        self.__number = dic["number"]
        self.__floatNumber = dic["float_number"]
        f.close()
~~~

#### fraction_collection
~~~python
from fraction import *

class FractionCollection:
    """Класс-контейнер, хранящий в себе дробные числа, манипулирующий с ними, и сохраняющий их в json формате"""
    def __init__(self, fractions):
        self._data = [None] * fractions
 
    def __str__(self):
        """Строковое представление колекции"""
        str = ''
        for i in range(len(self._data)):
            str += self._data[i].__str__() + " "
        return str
    
    def __setitem__(self, number, data):
        """Функция, реализующая запись элемента в коллекцию по индексу"""
        self._data[number] = data

    def __getitem__(self, number):
        """Функция, реализующая чтение элемента из коллекцию по индексу"""
        return self._data[number]
    
    def add(self, data):
        """Функция, реализующая добавление нового элемента в конец коллекции"""
        for i in range(len(self._data)):
            if(self._data[i] == None):
                self._data[i] = data
                break

    def remove(self, index):
        """Функция, реализующая удаление элемента из коллекции по индексу"""
        if(self._data[index]):
            self._data[index] = None

    def save(self, filename: str):
        """Метод, реализующий сохранение коллекции чисел в файл"""
        dict = {}
        for i in range(len(self._data)):
            dict.update({f'{i}': self._data[i].__str__()})
        f = open(filename+".json", "w")
        f.write(json.dumps(dict))
        f.close()

    def load(self, filename):
        """Метод, реализующий выгрузку коллекции чисел числа из файла"""
        f = open(filename+".json", "r")
        dic = json.loads(f.read())
        print(dic)
        for i in range(len(self._data)):
            if(dic[str(i)] == "None"):
                self._data[i] = None
                continue
            self._data[i] = dic[str(i)]
        f.close()

~~~


### Задание 2
Билеты
выстройте классы в иерархию, продумайте их общие и отличительные
характеристики и действия;
•
добавьте собственную реализацию методов базового класса в каждый
из классов, предусмотрев:
o необходимые параметры для базовых методов (например, в метод
воспроизведения в Dvd-плеере можно передать абстрактный
DVD-диск);
o необходимые поля для функционирования базовых методов
(например, при остановке Dvd-плеера имеет смысл сохранить
текущую позицию воспроизведения); классы должны содержать
как минимум по одному общедоступному, не общедоступному и
закрытому полю/методу;
o вывод на экран работы метода (например, вызов метода остановки
в Dvd-плеере должен сообщать на экране, что плеер установлен
на определенной позиции).
•
по желанию добавьте собственные методы в классы иерархии.
Реализуйте все классы в отдельном модуле, а также создайте main.py,
который бы тестировал все его возможности.
По согласованию иерархия может быть расширена или выбрана
самостоятельная индивидуальная тема для данной задачи.
При выполнении задания необходимо построить UML-диаграмма
классов приложения

#### Решение

#### ticket
~~~python
from abc import *
from datetime import *

class Ticket:
    """Базовый класс билетов, определяющий общее поле имени владельца и функции списания проезда"""
    def __init__(self, owner: str):
        self._owner: str = owner

    @abstractmethod
    def off_a_trip(self): pass
    """Абстрактная функция списания проезда"""
            
~~~

#### ticketArrive
~~~python
from ticket import *

class TicketArrive(Ticket):
    """Класс одноразового проездного, который имеет поле даты валидности и саму валидность, также реализует единичное списание билета"""
    def __init__(self, owner: str, legal_to: int):
        super().__init__(owner)
        self.__date: date = date.today() + timedelta(days=legal_to)
        self._isValid: bool = True

    def off_a_trip(self):
        """Единичное списание билета"""
        if(self.__date >= date.today() and self._isValid):
            print(f"Билет владельца {self._owner} использован!")
            self._isValid = False
        else:
            print(f"Срок действия билета истек или билет более недоступен")
            self._isValid = False

    def __str__(self):
        """Строковое представление билета"""
        if(self._isValid):
            return f"Владелец {self._owner}, действителен до {self.__date}."
        else:
            return f"Билет более недействителен, офромите новый"
            
~~~

#### unlimitedTicket
~~~python
from ticket import *

class UnlimitedTicket(Ticket):
    """Класс, представляющий безлимитный билет с полями счета билета, времени валидности и самой валидности"""
    def __init__(self, owner: str, legal_to: int, account: float):
        super().__init__(owner)
        self.__account: float = account
        self.__date: date = date.today() + timedelta(days=legal_to)
        if(self.__account < 500):
            self._isValid: bool = False
        else:
            self._isValid: bool = True

    def off_a_trip(self):
        """Проверка на валидность билета, ничего не списывается, т.к. билет бизлемитный"""
        if(self.__date >= date.today() and self._isValid):
            print(f"Безлимитный билет владельца {self._owner} использован.")
        elif(self.__date < date.today() and self._isValid):
            print("Действие билета законченно, пополните счет, чтобы продлить пользование")
            self.__account -= 500
            if(self.__account < 500):
                self._isValid = False
        else:
            print(f"На счете не хватает {500 - self.__account}, пополните счет билета, чтобы продолжить пользование")
    
    def upAccout(self, cash: float):
        """Функция, реализующая пополнение аккаунта"""
        self.__account += cash
        if(self.__account >= 500):
            self._isValid = True

    def __str__(self):
        """Строковое представление билета"""
        if(self._isValid):
            return f"Владелец {self._owner}, действителен до {self.__date}, денег на счете {self.__account}"
        else:
            return f"Билет более недействителен, офромите новый"
            
~~~

#### restrictionTicket
~~~python
from ticket import *

class RestrictionsTicket(Ticket):
    """Класс, представляющий ограниченного билет с полями счета билета и стоимости проезда"""
    def __init__(self, owner: str, account: float):
        super().__init__(owner)
        self._account: float = account
        self._cost = 100

    def off_a_trip(self):
        """С билета списываются деньги за каждую поездку"""
        if(self._account - self._cost >= 0):
            print(f"Билет владельца {self._owner} использован, списанно {self._cost}")
            self._account -= self._cost
        else:
            print("На счете недостаточно средств для поездки")
    
    def upAccout(self, cash: float):
        """Функция, реализующая пополнение аккаунта"""
        self._account += cash

    def __str__(self):
        """Строковое представление билета"""
        return f"Владелец {self._owner}, денег на счете {self._account}, хватит на {self._account // self._cost} поездок"
~~~

#### restrictionTravelTicket
~~~python
from restrictionsTicket import *

class RestrictionsTravelTicket(RestrictionsTicket):
    """Класс, представляющий ограниченного билет с полями счета билета и стоимости проезда, а также ограниченный по времени"""
    def __init__(self, owner: str, account: float, legal_to: int):
        super().__init__(owner, account)
        self.__date: date = date.today() + timedelta(days=legal_to)

    def off_a_trip(self):
        """Списывает деньги и проверят, валидный ли еще билет"""
        if(self._account - self._cost >= 0 and self.__date >= date.today()):
            print(f"Билет владельца {self._owner} использован, списанно {self._cost}")
            self._account -= self._cost
        elif(self._account - self._cost < 0 and self.__date >= date.today()):
            print("Для проезда недостаточно средств")
        else:
            print("Проездной более недоступен, срок действия истек")

    def __str__(self):
        """Строковое представление билета"""
        if(self.__date >= date.today()):
            return f"Владелец {self._owner}, действителен до {self.__date}, денег на счете {self._account}, хватит на {self._account // self._cost} поездок"
        else:
            return f"Билет более недействителен, оформите новый"
~~~


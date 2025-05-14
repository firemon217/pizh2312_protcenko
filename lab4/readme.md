# Лабораторная по ООП №4
## Практическая работа 
### Задание 1

Банк предлагает ряд вкладов для физических лиц:
•
Срочный вклад: расчет прибыли осуществляется по формуле простых
процентов;
•
Бонусный вклад: бонус начисляется в конце периода как % от прибыли,
если вклад больше определенной суммы;
• Вклад с капитализацией процентов.
Реализуйте приложение, которое бы позволило подобрать клиенту вклад
по заданным параметрам.
При выполнении задания необходимо построить UML-диаграмма
классов приложения

#### Решение

#### bank
~~~python
import abc

class Bank:
    """Класс банк, определяющий поля личного счета и счета депозита. 
    Реализует методы пополнения счета, вывод объекта счета и определяет несколько абстрактных методов, 
    определенных в наследуеммых классах"""
    def __init__(self, account: float):
        self._account: float = account
        self._deposit = 0
    
    def topUpAccount(self, cash: float) -> None:
        """Пополняет личный счет на определенную сумму"""
        self._account += cash

    @abc.abstractmethod
    def topUpDeposit(self, cash: float) -> None: 
        """Абстрактный метод, определящий пополнение депозитного счета"""
        pass

    @abc.abstractmethod
    def withdrawFromDeposit(self, cash: float) -> None: 
        """Абстрактный метод, определяющий вывод средств с депозитного счета на личный счет"""
        pass

    @abc.abstractmethod
    def interestAccrualOnDeposit(self) -> None: 
        """Абстрактный метод, определяющий расчет повышения депозита на определенный процент"""
        pass

    def __str__(self):
        """Строковое представление объекта счета"""
        return str(self._account) + " " + str(self._deposit)
~~~

#### bonusDeposit
~~~python
from bank import *

class BonusDeposit(Bank):
    """Класс бонусного депозита, определяющий поля процента депозита, рекордной суммы, которую необходимо достичь ждля начисления процентов 
    и счета депозита без процентов. Реализует пополнение депозита, определение бонусного депозита и снятие денег с депозита"""

    def __init__(self, account: float, procent: float, recordSum: float):
        super().__init__(account)
        self.__procent: float = procent
        self.__recordSum: float = recordSum
        self.__depositSum: float = 0

    def interestAccrualOnDeposit(self) -> None:
        """Определяет увеличение депозита на заданный процент, если достигнута рекордная сумма"""
        if(self._deposit >= self.__recordSum):
            self._deposit += self.__depositSum * self.__procent / 100

    def topUpDeposit(self, cash: float) -> None:
        """Метод, определящий пополнение депозитного счета"""
        if(self._account >= cash):
            self._deposit += cash
            self._account -= cash
            self.__depositSum += cash
        else:
            print("Недостаточно средств, чтобы положить такую сумму на депозит")

    def withdrawFromDeposit(self, cash: float) -> None:
        """Метод, определяющий вывод средств с депозитного счета на личный счет"""
        if(self._deposit >= cash):
            self._deposit -= cash
            self.__depositSum -= cash
            self._account += cash
        else:
            print("Недостаточно средств на счету депозита, чтобы перевести такую сумму на ваш личный счет")
~~~

#### capitalizationDeposit
~~~python
from bank import *

class CapitalizationProcentDeposti(Bank):
    """Класс депозита с капитализацией, определяющий поля процента депозита.
    Реализует пополнение депозита, определение увеличение депозита и начисленных процентов на процент и снятие денег с депозита"""
    def __init__(self, account: float, procent: float):
        super().__init__(account)
        self.__procent: float = procent

    def interestAccrualOnDeposit(self) -> None:
        """Определяет увеличение депозита и начисленных процентов на заданный процент"""
        self._deposit += self._deposit * self.__procent / 100

    def topUpDeposit(self, cash: float) -> None:
        """Метод, определящий пополнение депозитного счета"""
        if(self._account >= cash):
            self._deposit += cash
            self._account -= cash
        else:
            print("Недостаточно средств, чтобы положить такую сумму на депозит")

    def withdrawFromDeposit(self, cash: float) -> None:
        """Метод, определяющий вывод средств с депозитного счета на личный счет"""
        if(self._deposit >= cash):
            self._deposit -= cash
            self._account += cash
        else:
            print("Недостаточно средств на счету депозита, чтобы перевести такую сумму на ваш личный счет")
~~~

#### urgentDeposit
~~~python
from bank import *

class UrgentDeposit(Bank):
    """Класс простого депозита, определяющий поля процента депозита и счета депозита без процентов. 
    Реализует пополнение депозита, определение начисления процентов депозита и снятие денег с депозита"""
    def __init__(self, account: float, procent: float):
        super().__init__(account)
        self.__procent: float = procent
        self.__depositSum = 0

    def interestAccrualOnDepfrom bank import *

class CapitalizationProcentDeposti(Bank):
    """Класс депозита с капитализацией, определяющий поля процента депозита.
    Реализует пополнение депозита, определение увеличение депозита и начисленных процентов на процент и снятие денег с депозита"""
    def __init__(self, account: float, procent: float):
        super().__init__(account)
        self.__procent: float = procent

    def interestAccrualOnDeposit(self) -> None:
        """Определяет увеличение депозита и начисленных процентов на заданный процент"""
        self._deposit += self._deposit * self.__procent / 100

    def topUpDeposit(self, cash: float) -> None:
        """Метод, определящий пополнение депозитного счета"""
        if(self._account >= cash):
            self._deposit += cash
            self._account -= cash
        else:
            print("Недостаточно средств, чтобы положить такую сумму на депозит")

    def withdrawFromDeposit(self, cash: float) -> None:
        """Метод, определяющий вывод средств с депозитного счета на личный счет"""
        if(self._deposit >= cash):
            self._deposit -= cash
            self._account += cash
        else:
            print("Недостаточно средств на счету депозита, чтобы перевести такую сумму на ваш личный счет")очно средств на счету депозита, чтобы перевести такую сумму на ваш личный счет")
~~~

### Задание 2

Выберите класс под номером № (Таблица 1), где № Ваш порядковый
номер в журнале. При превышении порядка номера отчет ведется сначала по
циклу.
Прежде чем перейти к написанию кода:
изучите предметную область объекта и доступные операции;
для каждого поля и метода продумайте его область видимости, а также
необходимость использования свойств.
При реализации класс должен содержать:
специальные методы:
o init＿(self, …) - инициализация с необходимыми параметрами;
str (self) - представление объекта в удобном для человека виде;

#### Решение

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
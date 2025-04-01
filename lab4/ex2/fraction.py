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

            
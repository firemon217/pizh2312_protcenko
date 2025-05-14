from romanNumber import *

class Roman:
    """
    Класс, представляющий из себя набор функций для работы с римскими числами
    Реализует в себе методы для преобразования чисел, и работы с ними
    """
    def __init__(self, number: int):
        self.__roman: RomanNumber = RomanNumber(number)
    

    @staticmethod 
    def _reform(number: int):
        """
        Метод, который преобразует любое число в римское. Возвращает строку с римскими цифрами 
        """
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

    @staticmethod 
    def prereform(number: str):
        """
        Метод для преобразования римский чисел в обычное представление. Возвращает целочисленное число
        """
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

    def get_number(self):
        """
        Позволяет получить число, преображенное в римское
        """
        return self.__roman.get_intNumber()
    
    def __add__(self, other):
        """
        Метод суммы двух римских чисел, возвращает число обычного представления
        """
        return RomanNumber(self.__roman.get_intNumber() + other.__roman.get_intNumber())

    def __sub__(self, other):
        """
        Метод разности двух римских чисел, возвращает число обычного представления
        """
        return RomanNumber(self.__roman.get_intNumber() + other.__roman.get_intNumber())

    def __mul__(self, other):
        """
        Метод перемножения двух римских чисел, возвращает число обычного представления
        """
        return RomanNumber(self.__roman.get_intNumber() + other.__roman.get_intNumber())

    def __floordiv__(self, other):
        """
        Метод деления двух римских чисел, возвращает число обычного представления
        """
        return RomanNumber(self.__roman.get_intNumber() + other.__roman.get_intNumber())
    
    def __str__(self):
        """
        Метод вывод всех представлений числа
        """
        return self.__roman
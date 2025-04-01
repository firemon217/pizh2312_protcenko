from roman import *

class RomanNumber():
    """
    Класс, представляющий собой римское число и его обычный аналог. Наследуется от класса Roman
    """
    def __init__(self, intNumber: int):
        self.__intNumber: int = intNumber
        self.__rimNumber: str = Roman._reform(intNumber)

    def get_intNumber(self):
        """
        Метод для получения целочисленного представления числа
        """
        return self.__intNumber
    
    def get_rimNumber(self):
        """
        Метод для получения римского числа
        """
        return self.__rimNumber

    def __str__(self):
        """
        Метод вывода строкового формата двух представлений числа
        """
        return str(self.__intNumber) + " - " + self.__rimNumber
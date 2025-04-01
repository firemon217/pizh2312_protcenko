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
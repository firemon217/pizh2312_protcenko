from ticket import *

class RestrictionsTicket(Ticket):
    """Класс, представляющий ограниченного билет с полями счета билета и стоимости проезда"""
    def __init__(self, owner: str, account: float):
        super().__init__(owner)
        self._account: float = account
        self._cost: float = 100

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
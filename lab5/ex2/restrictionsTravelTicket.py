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
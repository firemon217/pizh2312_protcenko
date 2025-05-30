from restrictionsTicket import RestrictionsTicket
from datetime import date, timedelta

class RestrictionsTravelTicket(RestrictionsTicket):
    def __init__(self, owner: str, account: float, legal_to: int):
        super().__init__(owner, account)
        self.__date: date = date.today() + timedelta(days=legal_to)

    def off_a_trip(self):
        if self._account >= self._cost and self.__date >= date.today():
            print(f"Билет владельца {self._owner} использован, списано {self._cost}")
            self._account -= self._cost
        elif self._account < self._cost and self.__date >= date.today():
            print("Недостаточно средств")
        else:
            print("Срок действия билета истёк")

    def __str__(self):
        if self.__date >= date.today():
            return f"Владелец {self._owner}, действителен до {self.__date}, денег на счете {self._account}, хватит на {self._account // self._cost} поездок"
        else:
            return "Билет более недействителен, оформите новый"

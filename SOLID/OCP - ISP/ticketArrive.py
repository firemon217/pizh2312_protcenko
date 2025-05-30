from ticket import Ticket
from datetime import date, timedelta

class TicketArrive(Ticket):
    def __init__(self, owner: str, legal_to: int):
        super().__init__(owner)
        self.__date: date = date.today() + timedelta(days=legal_to)
        self._isValid: bool = True

    def off_a_trip(self):
        if self.__date >= date.today() and self._isValid:
            print(f"Билет владельца {self._owner} использован!")
            self._isValid = False
        else:
            print("Срок действия билета истек или уже использован")
            self._isValid = False

    def __str__(self):
        if self._isValid:
            return f"Владелец {self._owner}, действителен до {self.__date}"
        else:
            return "Билет более недействителен, оформите новый"

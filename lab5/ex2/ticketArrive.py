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
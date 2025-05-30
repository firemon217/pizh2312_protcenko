from ticket import Ticket, Rechargeable
from datetime import date, timedelta

class UnlimitedTicket(Ticket, Rechargeable):
    def __init__(self, owner: str, legal_to: int, account: float):
        super().__init__(owner)
        self.__account: float = account
        self.__date: date = date.today() + timedelta(days=legal_to)
        self._isValid: bool = self.__account >= 500

    def off_a_trip(self):
        if self.__date >= date.today() and self._isValid:
            print(f"Безлимитный билет владельца {self._owner} использован.")
        elif self.__date < date.today() and self._isValid:
            print("Срок действия билета истёк, списываю 500 за продление...")
            self.__account -= 500
            self._isValid = self.__account >= 500
        else:
            print(f"Недостаточно средств для продолжения, не хватает {500 - self.__account}")

    def up_account(self, cash: float):
        self.__account += cash
        if self.__account >= 500:
            self._isValid = True

    def __str__(self):
        if self._isValid:
            return f"Владелец {self._owner}, действителен до {self.__date}, денег на счете {self.__account}"
        else:
            return "Билет более недействителен, оформите новый"

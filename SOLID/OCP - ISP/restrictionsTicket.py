from ticket import Ticket, Rechargeable

class RestrictionsTicket(Ticket, Rechargeable):
    def __init__(self, owner: str, account: float):
        super().__init__(owner)
        self._account: float = account
        self._cost: float = 100

    def off_a_trip(self):
        if self._account >= self._cost:
            print(f"Билет владельца {self._owner} использован, списано {self._cost}")
            self._account -= self._cost
        else:
            print("На счете недостаточно средств для поездки")

    def up_account(self, cash: float):
        self._account += cash

    def __str__(self):
        return f"Владелец {self._owner}, денег на счете {self._account}, хватит на {self._account // self._cost} поездок"

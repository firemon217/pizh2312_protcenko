from abc import ABC, abstractmethod
from datetime import date, timedelta

class Ticket(ABC):
    """Интерфейс всех билетов: только списание поездки"""
    def __init__(self, owner: str):
        self._owner: str = owner

    @abstractmethod
    def off_a_trip(self): pass


class Rechargeable(ABC):
    """Интерфейс для пополняемых билетов"""
    @abstractmethod
    def up_account(self, cash: float): pass

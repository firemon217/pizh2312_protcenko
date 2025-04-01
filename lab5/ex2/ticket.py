from abc import *
from datetime import *

class Ticket:
    """Базовый класс билетов, определяющий общее поле имени владельца и функции списания проезда"""
    def __init__(self, owner: str):
        self._owner: str = owner

    @abstractmethod
    def off_a_trip(self): pass
    """Абстрактная функция списания проезда"""
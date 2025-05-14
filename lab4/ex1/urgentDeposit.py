from bank import *

class UrgentDeposit(Bank):
    """Класс простого депозита, определяющий поля процента депозита и счета депозита без процентов. 
    Реализует пополнение депозита, определение начисления процентов депозита и снятие денег с депозита"""
    def __init__(self, account: float, procent: float):
        super().__init__(account)
        self.__procent: float = procent
        self.__depositSum = 0

    def interestAccrualOnDeposit(self, days: int) -> None:
        """Определяет увеличение депозита на заданный процент с учетом дней, пополнения депозита"""
        self._deposit += (self.__depositSum * self.__procent * (days / 365)) / 100

    def topUpDeposit(self, cash: float) -> None:
        """Метод, определящий пополнение депозитного счета"""
        if(self._account >= cash):
            self._deposit += cash
            self._account -= cash
            self.__depositSum += cash
        else:
            print("Недостаточно средств, чтобы положить такую сумму на депозит")

    def withdrawFromDeposit(self, cash: float) -> None:
        if(self._deposit >= cash):
            self._deposit -= cash
            self._account += cash
            self.__depositSum -= cash
        else:
            print("Недостаточно средств на счету депозита, чтобы перевести такую сумму на ваш личный счет")
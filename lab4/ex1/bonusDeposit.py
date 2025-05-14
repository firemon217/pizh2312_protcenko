from bank import *

class BonusDeposit(Bank):
    """Класс бонусного депозита, определяющий поля процента депозита, рекордной суммы, которую необходимо достичь ждля начисления процентов 
    и счета депозита без процентов. Реализует пополнение депозита, определение бонусного депозита и снятие денег с депозита"""

    def __init__(self, account: float, procent: float, recordSum: float):
        super().__init__(account)
        self.__procent: float = procent
        self.__recordSum: float = recordSum
        self.__depositSum: float = 0

    def interestAccrualOnDeposit(self) -> None:
        """Определяет увеличение депозита на заданный процент, если достигнута рекордная сумма"""
        if(self._deposit >= self.__recordSum):
            self._deposit += self.__depositSum * self.__procent / 100

    def topUpDeposit(self, cash: float) -> None:
        """Метод, определящий пополнение депозитного счета"""
        if(self._account >= cash):
            self._deposit += cash
            self._account -= cash
            self.__depositSum += cash
        else:
            print("Недостаточно средств, чтобы положить такую сумму на депозит")

    def withdrawFromDeposit(self, cash: float) -> None:
        """Метод, определяющий вывод средств с депозитного счета на личный счет"""
        if(self._deposit >= cash):
            self._deposit -= cash
            self.__depositSum -= cash
            self._account += cash
        else:
            print("Недостаточно средств на счету депозита, чтобы перевести такую сумму на ваш личный счет")
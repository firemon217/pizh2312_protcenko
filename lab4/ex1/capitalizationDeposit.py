from bank import *

class CapitalizationProcentDeposti(Bank):
    """Класс депозита с капитализацией, определяющий поля процента депозита.
    Реализует пополнение депозита, определение увеличение депозита и начисленных процентов на процент и снятие денег с депозита"""
    def __init__(self, account: float, procent: float):
        super().__init__(account)
        self.__procent: float = procent

    def interestAccrualOnDeposit(self) -> None:
        """Определяет увеличение депозита и начисленных процентов на заданный процент"""
        self._deposit += self._deposit * self.__procent / 100

    def topUpDeposit(self, cash: float) -> None:
        """Метод, определящий пополнение депозитного счета"""
        if(self._account >= cash):
            self._deposit += cash
            self._account -= cash
        else:
            print("Недостаточно средств, чтобы положить такую сумму на депозит")

    def withdrawFromDeposit(self, cash: float) -> None:
        """Метод, определяющий вывод средств с депозитного счета на личный счет"""
        if(self._deposit >= cash):
            self._deposit -= cash
            self._account += cash
        else:
            print("Недостаточно средств на счету депозита, чтобы перевести такую сумму на ваш личный счет")
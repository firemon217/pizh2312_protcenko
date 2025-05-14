import abc

class Bank:
    """Класс банк, определяющий поля личного счета и счета депозита. 
    Реализует методы пополнения счета, вывод объекта счета и определяет несколько абстрактных методов, 
    определенных в наследуеммых классах"""
    def __init__(self, account: float):
        self._account: float = account
        self._deposit = 0
    
    def topUpAccount(self, cash: float) -> None:
        """Пополняет личный счет на определенную сумму"""
        self._account += cash

    @abc.abstractmethod
    def topUpDeposit(self, cash: float) -> None: 
        """Абстрактный метод, определящий пополнение депозитного счета"""
        pass

    @abc.abstractmethod
    def withdrawFromDeposit(self, cash: float) -> None: 
        """Абстрактный метод, определяющий вывод средств с депозитного счета на личный счет"""
        pass

    @abc.abstractmethod
    def interestAccrualOnDeposit(self) -> None: 
        """Абстрактный метод, определяющий расчет повышения депозита на определенный процент"""
        pass

    def __str__(self):
        """Строковое представление объекта счета"""
        return str(self._account) + " " + str(self._deposit)

    

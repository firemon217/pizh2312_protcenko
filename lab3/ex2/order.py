class Order:
    """ Класс Order хранит заказанные пиццы и их количество. """
    
    def __init__(self):
        self.__pizzas = []
    
    def __str__(self):
        return f"Заказ: {[pizza.name for pizza in self.__pizzas]}, Количество: {len(self.__pizzas)}"
    
    def add_pizza(self, pizza):
        """ Добавляет пиццу в заказ. """
        self.__pizzas.append(pizza)
    
    def total_price(self):
        """ Подсчитывает общую сумму заказа. """
        return sum(pizza.price for pizza in self.__pizzas)
    
    def execute(self):
        """ Выполняет заказ: готовит, выпекает, режет и упаковывает пиццы. """
        for pizza in self.__pizzas:
            pizza.prepare()
            pizza.bake()
            pizza.cut()
            pizza.box()
        print(f"Заказ выполнен! Общая стоимость: {self.total_price()}₽")
        self.__pizzas.clear()
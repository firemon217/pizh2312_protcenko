from pizza import *
from order import *

class Terminal:
    """ Терминал для оформления заказа. """
    
    def __init__(self):
        self.__menu = [PizzaPepperoni(), PizzaBarbecue(), PizzaSeafood()]
        self.__current_order = Order()
    
    def show_menu(self):
        """ Отображает доступные пиццы. """
        print("Меню пицц:")
        for idx, pizza in enumerate(self.__menu, 1):
            print(f"{idx}. {pizza.name} - {pizza.price}₽")
    
    def add_pizza_to_order(self, choice):
        """ Добавляет выбранную пиццу в заказ. """
        if 1 <= choice <= len(self.__menu):
            self.__current_order.add_pizza(self.__menu[choice - 1])
            print(f"Добавлена {self.__menu[choice - 1].name}.")
        else:
            print("Ошибка выбора!")
    
    def finalize_order(self):
        """ Принимает оплату и завершает заказ. """
        print(f"К оплате: {self.__current_order.total_price()}₽")
        print("Оплата принята.")
        self.__current_order.execute()
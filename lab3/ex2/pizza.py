class Pizza:
    """
    Класс Pizza описывает пиццу с ее основными характеристиками:
    название, тип теста, соус, начинка и стоимость.
    """
    
    def __init__(self, name, dough, sauce, filling, price):
        self.__name = name
        self.__dough = dough
        self.__sauce = sauce
        self.__filling = filling
        self.__price = price
    
    def __str__(self):
        return (f"Пицца: {self.name}, Тесто: {self.dough}, Соус: {self.sauce}, "
                f"Начинка: {', '.join(self.filling)}, Цена: {self.price}₽")
    
    @property
    def name(self): return self.__name
    @name.setter
    def name(self, value): self.__name = value
    
    @property
    def dough(self): return self.__dough
    @dough.setter
    def dough(self, value): self.__dough = value
    
    @property
    def sauce(self): return self.__sauce
    @sauce.setter
    def sauce(self, value): self.__sauce = value
    
    @property
    def filling(self): return self.__filling
    @filling.setter
    def filling(self, value): self.__filling = value
    
    @property
    def price(self): return self.__price
    @price.setter
    def price(self, value): self.__price = value
    
    def prepare(self): print(f"Готовим {self.name}...")
    def bake(self): print(f"Выпекаем {self.name}...")
    def cut(self): print(f"Режем {self.name} на кусочки...")
    def box(self): print(f"Упаковываем {self.name}...")
    

class PizzaPepperoni(Pizza):
    """ Пицца Пепперони """
    def __init__(self):
        super().__init__("Пепперони", "Тонкое тесто", "Томатный соус", ["Пепперони", "Сыр"], 300)


class PizzaBarbecue(Pizza):
    """ Пицца Барбекю """
    def __init__(self):
        super().__init__("Барбекю", "Толстое тесто", "Соус барбекю", ["Курица", "Лук", "Соус барбекю"], 350)


class PizzaSeafood(Pizza):
    """ Пицца с морепродуктами """
    def __init__(self):
        super().__init__("Морепродукты", "Тонкое тесто", "Белый соус", ["Креветки", "Кальмары", "Мидии"], 450)

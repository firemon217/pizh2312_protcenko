import math #Подключение библиотеки с мат функциями

class Windows: #Класс окна
    def __init__(self, width, height):
        self.area = width * height #В параметрах площадь окна

class Room: #Класс комнаты
    def __init__(self, length, width, height): #В параметрах высота, длина, ширина комнаты и массив окон (по умолчанию пустой)
        self.length = length
        self.width = width
        self.height = height
        self.windows = []

    def add_window(self, width, height): #Добавляем окно в нашу комнату
        if(height > self.height or (width > self.width and width > self.length)): #Проверяем, помещается ли окно
            print("Невозможно установить такое окно")
        else:
            if(self.work_area() < width * height): #Проверяем, есть ли еще место под окно
                print("Места не хватит")
            else:
                self.windows.append(Windows(width, height)) #Добавляем окно в случае успеха

    def total_wall_area(self): #Площадь стен
        return self.height * 2 * (self.length + self.width)

    def work_area(self): #Площадь работы
        total = self.total_wall_area()
        for window in self.windows: #Вычитаем площадь окно из стен
            total -= window.area
        return total

    def wallpappers_needed(self, wallpappers_length, wallpappers_width): #Проверяем, сколько обоев нам требуется
        return math.ceil(self.work_area() / (wallpappers_length * wallpappers_width))
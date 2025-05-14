from room import Room

length = float(input("Введите длину комнаты: ")) #Вводим длину комнаты
width = float(input("Введите ширину комнаты: ")) #Вводим ширину комнаты
height = float(input("Введите высоту комнаты: ")) #Вводим высоту комнаты

room = Room(length, width, height) #Создаем экземпляр комнаты

while True:import math

class Windows:
    def __init__(self, width, height):
        self.area = width * height

class Room:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
        self.windows = []

    def add_window(self, width, height):
        if(height > self.height or (width > self.width and width > self.length)):
            print("Невозможно установить такое окно")
        else:
            if(self.work_area() < width * height):
                print("Места не хватит")
            else:
                self.windows.append(Windows(width, height))

    def total_wall_area(self):
        return self.height * 2 * (self.length + self.width)

    def work_area(self):
        total = self.total_wall_area()
        for window in self.windows:
            total -= window.area
        return total

    def wallpappers_needed(self, wallpappers_length, wallpappers_width):
        return math.ceil(self.work_area() / (wallpappers_length * wallpappers_width))
    choice = int(input("Добавить окно? Да - 1, Нет - 0): ")) #Выбор, добавить ли окно в комнату
    if choice: #Если выбрали
        w = float(input("Ширина окна: ")) #Ввроим ширину нужного окна
        h = float(input("Высота окна: ")) #Вводим высоту нужного окна
        room.add_window(w, h) #Добавляем окно
    else:
        break

wallpappers_length = float(input("Длина одного рулона: ")) #Вводим длину нашего рулона обоев
wallpappers_width = float(input("Ширина одного рулона: ")) #Вводим ширину нашего рулона обоев

print("\nРезультаты:") #Результат работы
print(f"Площадь для оклейки: {room.work_area()} кв.м") 
print(f"Требуется рулонов: {room.wallpappers_needed(wallpappers_length, wallpappers_width)}")
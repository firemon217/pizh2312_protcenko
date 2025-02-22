import math

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

room = Room(5, 7, 2.8)

room.add_window(3, 1)

print(room.wallpappers_needed(10, 1))
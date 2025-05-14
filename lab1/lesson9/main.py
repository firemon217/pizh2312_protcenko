from room import Room

length = float(input("Введите длину комнаты (м): "))
width = float(input("Введите ширину комнаты (м): "))
height = float(input("Введите высоту комнаты (м): "))

room = Room(length, width, height)

while True:
    choice = int(input("Добавить окно? (да - 1/нет - 0): "))
    if choice:
        w = float(input("Ширина окна (м): "))
        h = float(input("Высота окна (м): "))
        room.add_window(w, h)
    else:
        break

wallpappers_length = float(input("Длина одного рулона (м): "))
wallpappers_width = float(input("Ширина одного рулона (м): "))

print("\nРезультаты:")
print(f"Площадь для оклейки: {room.work_area()} м²")
print(f"Требуется рулонов: {room.wallpappers_needed(wallpappers_length, wallpappers_width)}")
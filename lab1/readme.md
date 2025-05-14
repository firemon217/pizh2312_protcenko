# Лабораторная по ООП №1 урок
## Цель работы

Научиться создавать классы и объекты на языке python

## Практическая работа 
### Задание 2

Напишите программу по следующему описанию. Есть класс "Воин". От него создаются два
экземпляра-юнита. Каждому устанавливается здоровье в 100 очков. В случайном порядке они
бьют друг друга. Тот, кто бьет, здоровья не теряет. У того, кого бьют, оно уменьшается на 20
очков от одного удара. После каждого удара надо выводить сообщение, какой юнит атаковал, и
сколько у противника осталось здоровья. Как только у кого-то заканчивается ресурс здоровья,
программа завершается сообщением о том, кто одержал победу.

#### Решение

~~~python
import random

class Menu:
    def __init__(self):
        start = int(input("Хотите начать игру? 1 - да, 0 - нет\n"))
        if(start):
            self.hero = Warrior(input("Назовите своего героя\n"))
            self.game()

    def game(self):
        fight = int(input("Хотите ли вы сразиться? 1 - да, 0 - нет\n"))
        if(fight):
            self.enemy = Warrior("Враг Миша")
            while(self.enemy.health > 0 and self.hero.health > 0):
                chance = random.randint(0,1)
                if(chance):
                    print("Ты ударил врага")
                    self.enemy.health -= self.hero.damage
                else:
                    print("Враг ударил тебя")
                    self.hero.health -= self.enemy.damage
            if(self.hero.health <= 0):
                print("Ты проиграл")
            else:
                print("Ты победил")
                    


class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
    def __str__(self):
        return "This is " + str(self.name) + ", he is Warrior, he has health: " + str(self.health)

class Warrior(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.damage = 25
        if(not("Враг" in name)):
            print(self)
        else:
            print(self.name + " - одолейте его")

if __name__ == "__main__":
    menu = Menu()
~~~

### Задание 3

Помимо конструктора объектов в языках программирования есть обратный ему метод -
деструктор. Он вызывается, когда объект не создается, а уничтожается.
В языке программирования Python объект уничтожается, когда исчезают все связанные с ним
переменные или им присваивается другое значение, в результате чего связь со старым объектом
теряется. Удалить переменную можно с помощью команды языка del.
В
классах Python функцию деструктора выполняет метод ＿del ().
Напишите программу по следующему описанию:

1. Есть класс Person, конструктор которого принимает три параметра (не учитывая self) -
имя, фамилию и квалификацию специалиста. Квалификация имеет значение заданное по
умолчанию, равное единице.
2. У класса Person есть метод, который возвращает строку, включающую в себя всю
информацию о сотруднике.
3. Класс Person содержит деструктор, который выводит на экран фразу "До свидания,
мистер …" (вместо троеточия должны выводиться имя и фамилия объекта).
4. В основной ветке программы создайте три объекта класса Person. Посмотрите
информацию о сотрудниках и увольте самое слабое звено.
5. В конце программы добавьте функцию input(), чтобы скрипт не завершился сам, пока не
будет нажать Enter. Иначе вы сразу увидите как удаляются все объекты при завершении
работы программы.
В Python деструктор используется редко, так как интерпретатор и без него хорошо убирает
"мусор".

#### Решение

~~~python
class Person:
    def __init__(self, name, surname, experience = 1):
        self.name = name
        self.surname = surname
        self.experience = experience
    def info(self):
        return "Имя сотрудника - " + self.__str__() + ", стаж " + str(self.experience) + " лет."
    def __str__(self):
        return self.surname + " " + self.name
    def __del__(self):
        print("До свидания,", self)
   

if __name__ == "__main__":
    firstPerson = Person("Александр", "Кондратов", 25)
    secondPerson = Person("Максим", "Проценко", 23)
    thirdPerson = Person("Тимофей", "Аксенюк", -1)
    
    staff = [firstPerson, secondPerson, thirdPerson]

    del(thirdPerson)

    input()
~~~

### Задание 4

Разработайте программу по следующему описанию.
В некой игре-стратегии есть солдаты и герои. У всех есть свойство, содержащее уникальный
номер объекта, и свойство, в котором хранится принадлежность команде. У солдат есть метод
"иду за героем", который в качестве аргумента принимает объект типа "герой". У героев есть
метод увеличения собственного уровня.
В основной ветке программы создается по одному герою для каждой команды. В цикле
генерируются объекты-солдаты. Их принадлежность команде определяется случайно. Солдаты
разных команд добавляются в разные списки.
Измеряется длина списков солдат противоборствующих команд и выводится на экран. У героя,
принадлежащего команде с более длинным списком, поднимается уровень.
Отправьте одного из солдат первого героя следовать за ним. Выведите на экран
идентификационные номера этих двух юнитов.

#### Решение

~~~python
import random

class Unit:
    count = 0

    def __init__(self, team):
        Unit.count += 1
        self.id = Unit.count
        self.team = team

class Hero(Unit):
    def __init__(self, team):
        super().__init__(team)
        self.level = 1

    def level_up(self):
        self.level += 1

class Soldier(Unit):
    def __init__(self, team):
        super().__init__(team)

    def follow(self, hero):
        if isinstance(hero, Hero):
            print(f"Солдат {self.id} следует за героем {hero.id}")
        else:
            print(f"Солдат {self.id} не может следовать за не-героем!")

heroOne = Hero(1)
heroTwo = Hero(2)

teamOne = []
teamTwo = []

for _ in range(10):
    soldier = Soldier(random.choice([1, 2]))
    if soldier.team == 1:
        teamOne.append(soldier)
    else:
        teamTwo.append(soldier)

if len(teamOne) > len(teamTwo):
    heroOne.level_up()
elif len(teamOne) < len(teamTwo):
    heroTwo.level_up()

if teamOne:
    teamOne[0].follow(heroOne)
    print(f"ID солдата: {teamOne[0].id}, ID героя: {heroOne.id}")
else:
    print("В команде 1 нет солдат!")

~~~

### Задание 5

В качестве практической работы попробуйте самостоятельно перегрузить оператор сложения.
Для его перегрузки используется метод ＿add(). Он вызывается, когда объекты класса,
имеющего данный метод, фигурируют в операции сложения, причем с левой стороны. Это
значит, что в выражении а + b y объекта а должен быть метод ＿add (). Объект b может
быть чем угодно, но чаще всего он бывает объектом того же класса. Объект b будет
автоматически передаваться в метод ＿add＿() в качестве второго аргумента (первый - self).
Отметим, в Python также есть правосторонний метод перегрузки сложения - ＿add＿().
Согласно полиморфизму ООП, возвращать метод ＿add＿() может что угодно. Может вообще
ничего не возвращать, а "молча" вносить изменения в какие-то уже существующие объекты.
Допустим, в вашей программе метод перегрузки сложения будет возвращать новый объект того
же класса.

#### Решение

~~~python
class Triangle:
    def __init__(self, sideOne, sideTwo, sideThree):
        self.sideOne = sideOne
        self.sideTwo = sideTwo
        self.sideThree = sideThree

    def __add__(self, other):
        if isinstance(other, Triangle):
            return Triangle(self.sideOne + other.sideOne, self.sideTwo + other.sideTwo, self.sideThree + other.sideThree)
        raise TypeError("Сложение возможно только между объектами класса Triangle")

    def __str__(self):
        return f"Треугольник со сторонами {self.sideOne}, {self.sideTwo}, {self.sideThree}"

triOne = Triangle(2, 3, 4)
triTwo = Triangle(4, 5, 3)

triSum = triOne + triTwo

print(triSum)
~~~

### Задание 6

Разработайте класс с "полной инкапсуляцией", доступ к атрибутам которого и изменение
данных реализуются через вызовы методов. В объектно-ориентированном программировании
принято имена методов для извлечения данных начинать со слова get (взять), а имена методов, в
которых свойствам присваиваются значения, - со слова set (установить). Например, getField,
setField.

#### Решение

~~~python
class Incapsul:
    def __init__(self):
        self.__field = 0

    def get_field(self):
        return self.__field

    def set_field(self, value):
        self.__field = value

data = Incapsul()
data.set_field(100)
print(data.get_field())
~~~

### Задание 7

Приведенная выше программа имеет ряд недочетов и недоработок. Требуется исправить и
доработать, согласно следующему плану.
При вычислении оклеиваемой поверхности мы не "портим" поле self.square. В нем так и
остается полная площадь стен. Ведь она может понадобиться, если состав списка wd изменится,
и придется заново вычислять оклеиваемую площадь.
Однако в классе не предусмотрено сохранение длин сторон, хотя они тоже могут понадобиться.
Например, если потребуется изменить одну из величин у уже существующего объекта. Площадь
же помещения всегда можно вычислить, если хранить исходные параметры. Поэтому сохранять
саму площадь в поле не обязательно.
Исправьте код так, чтобы у объектов Room были только четыре поля - width, length, height и wd.
Площади (полная и оклеиваемая) должны вычислять лишь при необходимости путем вызова
методов.
Программа вычисляет площадь под оклейку, но ничего не говорит о том, сколько потребуется
рулонов обоев. Добавьте метод, который принимает в качестве аргументов длину и ширину
одного рулона, а возвращает количество необходимых, исходя из оклеиваемой площади.
Разработайте интерфейс программы. Пусть она запрашивает у пользователя данные и выдает
ему площадь оклеиваемой поверхности и количество необходимых рулонов.

#### Решение

~~~python
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

~~~

### Задание 8

Напишите класс Snow по следующему описанию.
В конструкторе класса инициируется поле, содержащее количество снежинок, выраженное
целым числом.
Класс включает методы перегрузки арифметических операторов: ＿add＿() - сложение,
sub＿() - вычитание, ＿mul＿() - умножение, ＿truediv＿() - деление. В классе код этих
методов должен выполнять увеличение или уменьшение количества снежинок на число п или
n раз. Метод ＿truediv () перегружает обычное (/), а не целочисленное (//) деление. Однако
пусть в методе происходит округление значения до целого числа.
в
Класс включает метод makeSnow(), который принимает сам объект и число снежинок в ряду, а
возвращает строку вида "\*\*\*\*\*\n******\n*****", где количество снежинок между '\n' равно
переданному аргументу, а количество рядов вычисляется, исходя из общего количества
снежинок.
Вызов объекта класса Snow в нотации функции с одним аргументом, должен приводить к
перезаписи значения поля, в котором хранится количество снежинок, на переданное в качестве
аргумента значение.

#### Решение

~~~python
class Snow:
    def __init__(self, snowflake):
        self.snowflake = snowflake

    def __add__(self, n):
        return Snow(self.snowflake + n)

    def __sub__(self, n):
        return Snow(self.snowflake - n)

    def __mul__(self, n):
        return Snow(self.snowflake * n)

    def __truediv__(self, n):
        return Snow(round(self.snowflake / n))

    def __call__(self, new_snowflake):
        self.snowflake = new_snowflake

    def make_snow(self, row):
        rows = self.snowflake // row
        ost = self.snowflake % row
        return ('*' * row + '\n') * rows + ('*' * ost if ost else '')

snow = Snow(15)
snow + 5
print(snow.make_snow(5))

~~~

### Задание 9

В практической работе урока 7 "Композиция" требовалось разработать интерфейс
взаимодействия с пользователем. Разнесите сам класс и интерфейс по разным файлам. Какой из
них выполняет роль модуля, а какой - скрипта? Оба файла можно поместить в один каталог.

#### Решение

~~~python
#main.py

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

~~~

~~~python
#room.py

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

~~~

### Задание 10

Выполните полное документирование модуля, созданного в практической работе прошлого урока

#### Решение

~~~python
#main.py

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

~~~

~~~python
#room.py

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

~~~

### Задание 11

Может ли в этой программе ученик учиться без учителя? Если да, пусть научится чему-нибудь
сам.
Добавьте в класс Pupil метод, позволяющий ученику случайно "забывать" какую-нибудь часть
своих знаний.

#### Решение

~~~python
import random

class Data:
    def __init__(self, *info):
        self.info = list(info)

    def getitem (self, i):
        return self.info [i]
        
class Teacher:
    def __init__(self):
        self.knowledge = []

    def teach(self, info, *pupil):
        for i in pupil:
            i.take(info)

class Pupil:
    def __init__ (self):
        self.knowledge = []

    def take(self, info):
        self.knowledge.append(info)

    def forget(self):
        if self.knowledge:
            index = random.randint(0, len(self.knowledge)-1)
            del self.knowledge[index]

pupil = Pupil()
pupil.take("C#")
pupil.take("ООП")
pupil.take("SoftWare")
pupil.forget()
print(pupil.knowledge)

~~~
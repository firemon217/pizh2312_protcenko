# Лабораторная по ООП №2
## Практическая работа 
### Задание 1 - Вариант 10

Экземпляр класса инициализируется с аргументом name - именем котенка. Класс
реализует методы:
- to answer() - ответить: котенок через один раз отвечает да или нет, начинает с да. Метод
возвращает "moore-moore", если да, "meow-meow", если нет. Одновременно
увеличивается количество соответствующих ответов;
- number
yes() - количество ответов да;
number no() - количество ответов нет.

#### Решение

~~~python
import abc

class Talking(abc.ABC):
    @abc.abstractmethod
    def to_answer(self): pass
    @abc.abstractmethod
    def number_yes(self): pass
    @abc.abstractmethod
    def number_no(self): pass
    @abc.abstractmethod
    def i_am(self): pass

class Animals(Talking):
    def __init__(self, name, color):
        self._name = name
        self._yes = 0
        self._no = 0
        self._color = Color(color)

    def get_name(self):
        return self._name
    
    def to_answer(self): pass

    def number_yes(self):
        return self._yes

    def number_no(self):
        return self._no

    def i_am(self): pass

class Kitten(Animals):
    def __init__(self, name, color):
        super().__init__(name, color)
    def to_answer(self):
        if(self._no == self._yes):
            self._yes += 1
            return "meow-meow"
        else:
            self._no += 1
            return "mour-mour"
    def i_am(self):
        return f"I`am a Cat, my name is {self.get_name()}, I says 'yes' {self.number_yes()} times, no {self.number_no()}, and my color is {self._color.get_color()}"

class Doggy(Animals):
    def __init__(self, name, color):
        super().__init__(name, color)
    def to_answer(self):
        if(self._no == self._yes):
            self._yes += 1
            return "woaf-woaf"
        else:
            self._no += 1
            return "rrrraf"
    def i_am(self):
        return f"I`am a Dog, my name is {self.get_name()}, I says 'yes' {self.number_yes()} times, no {self.number_no()}, and my color is {self._color.get_color()}"

class Color:
    def __init__(self, color):
        self.__red = color[0]
        self.__green = color[1]
        self.__blue = color[2]
    def get_color(self):
        return f"[{self.__red}, {self.__green}, {self.__blue}]"
    

kitten = Kitten("Kitty", [255, 255, 255])
doggy = Doggy("Racks", [0, 0, 0])

print(kitten.to_answer())
print(kitten.to_answer())
print(kitten.to_answer())
print(kitten.i_am())

print(doggy.to_answer())
print(doggy.to_answer())
print(doggy.to_answer())
print(doggy.i_am())


~~~
from fraction import *

class FractionCollection:
    """Класс-контейнер, хранящий в себе дробные числа, манипулирующий с ними, и сохраняющий их в json формате"""
    def __init__(self, fractions):
        self._data = [None] * fractions
 
    def __str__(self):
        """Строковое представление колекции"""
        str = ''
        for i in range(len(self._data)):
            str += self._data[i].__str__() + " "
        return str
    
    def __setitem__(self, number, data):
        """Функция, реализующая запись элемента в коллекцию по индексу"""
        self._data[number] = data

    def __getitem__(self, number):
        """Функция, реализующая чтение элемента из коллекцию по индексу"""
        return self._data[number]
    
    def add(self, data):
        """Функция, реализующая добавление нового элемента в конец коллекции"""
        for i in range(len(self._data)):
            if(self._data[i] == None):
                self._data[i] = data
                break

    def remove(self, index):
        """Функция, реализующая удаление элемента из коллекции по индексу"""
        if(self._data[index]):
            self._data[index] = None

    def save(self, filename: str):
        """Метод, реализующий сохранение коллекции чисел в файл"""
        dict = {}
        for i in range(len(self._data)):
            dict.update({f'{i}': self._data[i].__str__()})
        f = open(filename+".json", "w")
        f.write(json.dumps(dict))
        f.close()

    def load(self, filename):
        """Метод, реализующий выгрузку коллекции чисел числа из файла"""
        f = open(filename+".json", "r")
        dic = json.loads(f.read())
        print(dic)
        for i in range(len(self._data)):
            if(dic[str(i)] == "None"):
                self._data[i] = None
                continue
            self._data[i] = dic[str(i)]
        f.close()


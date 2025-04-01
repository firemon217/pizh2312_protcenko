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
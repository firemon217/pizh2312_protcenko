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
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
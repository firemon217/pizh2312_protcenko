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
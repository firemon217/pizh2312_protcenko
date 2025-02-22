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

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
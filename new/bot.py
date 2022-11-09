import random

class Bot:
    bots = 0

    def __init__(self, name, life=50) -> None:
        self.name = name
        self.life = life

        Bot.bots += 1

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new):
        if not isinstance(new, str):
            raise TypeError("Name must be a string")
        else:
            self.__name = new

    @property
    def life(self):
        return self.__life

    
    @life.setter
    def life(self, value):
        if type(value) is not int:
            raise TypeError("Life must be an integer")
        elif value < 0:
            raise ValueError("Life must be >= 0")
        else:
            self.__life = value

    
    def __str__(self) -> str:
        return f"{self.name}"


# driver function
def startGame():
    bot1 = Bot("X")
    bot2 = Bot("Y")

    bots = [bot1, bot2]

    while True:
        choice = random.choice(bots)

        if choice == bot1:
            print("X deals Y 10 point!")
            bot2.life -= 10
        else:
            print("Y deals X 10 points!")
            bot1.life -= 10

        if bot1.life == 0:
            print("X out of life,dying...")
            print("Y wins")
            break

        elif bot2.life == 0:
            print("Y out of life, dying...")
            print("X wins")
            break

# startGame()
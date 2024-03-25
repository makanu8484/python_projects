from random import randint

x = randint(1, 6)

class Dices:
    def __init__(self, sides=6):
        self.sides = sides


    def roll(self):
        print("Rolling the dices:")
        for x in range(20):
            x = randint(1, self.sides)
            print("The dices rolled: " + str(x))


rolling_dices = Dices()
rolling_dices.roll()

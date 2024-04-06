from numpy.random import randint
class Utilities:
    def getUserInput(self):
        sides = int(input("How many sides per dice?"))
        dice = int(input("How many dices to throw?"))
        self.sides=sides
        self.dice = dice
        return sides,dice
    
    def roll(self, sides):
        return randint(1, sides)
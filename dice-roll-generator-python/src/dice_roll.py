from numpy.random import randint

class DiceRoll:
    def __init__(self):
        self.sides = int(input("How many sides per dice?"))
        self.dice = int(input("How many dices to throw?"))

    def roll(self):
        return randint(1, self.sides+1)
    
    def result(self):
        sum = 0
        while self.dice>0:
            result=int(self.roll())
            print(f"{result}")
            self.dice-=1
            sum+=result
        print(f"{sum}")

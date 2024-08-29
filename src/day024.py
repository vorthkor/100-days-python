# day24_100 days - infinity dice

import random

print("""
********************
* Infinity Dice 🎲 *
********************

""")

game = "yes"


def infinityDice(sides):
  number = random.randint(1,sides)
  print("You rolled ", number)


while game == "yes":

  side = int(input("How many sides?: "))

  infinityDice(side)
  
  game = input("Roll again? ")


print("bye!")
import random


print("""
⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️
⚔️ Character Stats Generator ⚔️
⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️

""")

again = "yes"

def infinityDice(sides):
  number = random.randint(1,sides)
  # print("You rolled ", number)
  return number


def sixAndEight():
  six = infinityDice(6)
  eight = infinityDice(8)
  return six * eight
  

while True:
  if again == "yes":
    name = input("Name your warrior: ")
    health = sixAndEight()
    print("Their health is: ",health,"hp")
  again = input("\n Play another? ")
  if again == "yes":
    print()
    continue
  elif again == "no":
    break
  else:
    print("Please answer yes or no")

print("bye!")

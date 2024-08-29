# day 28_100 days of code - Game Battle System

import time
import os
import random

pround = 1

# SUBROUTIUNES
def createCharacter():
  name = input("Name Your Legend:\n")
  c_race = input("Character Type (Human 👷, Elf 🧝, Dwarf 🧚, Gnome 🎅, Orc 🧟, Troll 🧌):\n")
  c_class = input("Character Type (Warrior 🗡️, Rogue 🥷, Wizard 🧙, Warlock 🔮, Druid 🐁):\n")
  return name,c_race,c_class


def rollStats():
  six_roll = rollSixDice()
  twelve_roll = rollTwelveDice()
  health = ((six_roll * twelve_roll)/2)+10
  strength = ((six_roll * twelve_roll)/2)+12
  return health,strength


def rollSixDice():
  return random.randint(1,6)

def rollTwelveDice():
  return random.randint(1,12)


def damage(stre1,stre2):
  if stre1 > stre2:
    sdiff = stre1 - stre2
  elif stre2 > stre1:
    sdiff = stre2 - stre1
  else:
    sdiff = 10
  ndamage = sdiff + 1
  return ndamage


def result(winner,loser,dmg,pround):
  if pround == 1:
    print(f"{winner} wins the first blow 🎉")
  else:
    print(f"{winner} wins round {pround} 🎊")
  print(f"{loser} takes a hit, with {dmg} damage 😵\n")


def newstats(winame,winh,losname,losh, pround):
  print(f"""
  {winame}
  🫀HEALTH: {winh}
  
  {losname}
  🫀HEALTH: {losh}\n""")
  
  if losh <= 0:
    print(f"Oh no {losname} has died! ☠️💀")
    print(f"{winame} 🏆 destroyed {losname} 👻 in {pround} rounds! 🤼")
    return 0
  else:
    return 1


# INIT
time.sleep(5)
os.system("clear")

print(" ⚔️ BATTLE TIME ⚔️ \n")

name,race,c_class = createCharacter()
health,strength = rollStats()

print(f"""
{name}
🫀HEALTH: {health}
🦾STRENGTH: {strength}\n""")

print("Who are they battling?\n")

name2,race2,c_class2 = createCharacter()
health2,strength2 = rollStats()

print(f"""
{name2}
🫀HEALTH: {health2}
🦾STRENGTH: {strength2}""")

time.sleep(5)
os.system("clear")

print("""⚔️ BATTLE TIME ⚔️
      The battle begins!\n""")

while True:
  play1 = rollSixDice()
  play2 = rollSixDice()
  if play1 > play2:
    dmg = damage(strength,strength2)
    health2 = health2 - dmg
    result(name,name2,dmg,pround)
    continue_play = newstats(name,health,name2,health2,pround)
  elif play2 > play1:
    dmg = damage(strength,strength2)
    health = health - dmg
    result(name2,name,dmg,pround)
    continue_play = newstats(name2,health2,name,health,pround)
  else:
    print("IT`S A TIE")
    continue_play = 1
  if continue_play == 1:
    pround = pround + 1
    print("And they're both standing for the next round!\n")
    time.sleep(5)
    os.system("clear")
    print("""
    ⚔️ BATTLE TIME ⚔️
  
    The battle continues!\n""")
  else:
    break

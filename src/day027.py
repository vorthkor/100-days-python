# day 27_100 days of code - Character generator

import time
import os
import random

GAME_ON = True


def createCharacter():
  name = input("Name Your Legend:\n")
  c_race = input("Character Type (Human, Elf, Dwarf, Gnome, Orc, Troll):\n")
  c_class = input("Character Type (Warrior, Rogue, Wizard, Warlock, Druid):\n")

  return name,c_race,c_class


def rollHealth():
  six_roll = random.randint(1,6)
  twelve_roll = random.randint(1,12)
  return ((six_roll * twelve_roll)/2)+10


def rollStrength():
  six_roll = random.randint(1,6)
  twelve_roll = random.randint(1,12)
  return ((six_roll * twelve_roll)/2)+12


while GAME_ON:
  os.system("clear")
  time.sleep(3)
  
  print(" ⚔️⚔️⚔️ Character Builder ⚔️⚔️⚔️ ")
  
  name,race,c_class = createCharacter()
  health = rollHealth()
  strength = rollStrength()
  
  print(f"""{name}
  HEALTH: {health}
  STRENGTH: {strength}
  May your name go down in Legend...""")

  again = input("Again?")
  if again == "No":
    GAME_ON = False
    
    
# day45_100 - TODOITTTTT

import os
import time

todo_list = []


def newColor(color, word):
  colors = {
    "red": f"\033[31m{word}\033[0m",
    "green": f"\033[32m{word}\033[0m",
    "yellow": f"\033[33m{word}\033[0m",
    "blue": f"\033[34m{word}\033[0m",
    "purple": f"\033[35m{word}\033[0m",
  }
  return colors.get(color,f"\033[0m{word}\033[0m")


def menuAdd():
  name = input("What to do?: ")
  due = input("When it is due by?: ")
  priority = input("What is the priority?: ")
  row = [name, due, priority]
  todo_list.append(row)
  


def menuView():
  which_view = int(input("""
  1: view all
  2: view priority
  : """))
  os.system("clear")
  if which_view == 1:
    print()
    print("✅ To Do List ✅")
    for row in todo_list:
      for item in row:
        print(f"{item:^10}", end=" | ")
      print()
    print() 
    time.sleep(3)
  else:
    which_prio = input("""
    1: high
    2: medium
    3: low 
    : """)
    for row in todo_list:
      if which_prio in row:
        for item in row:
          print(f"{item:^10}", end=" | ")
    print() 
    time.sleep(3)


def menuEdit():
  print()
  item = input("Which item do you want to edit?")
  for row in todo_list:
    if item in row:
      todo_list.remove(row)
  menuAdd()
  print() 


def menuRemove():
  print()
  item = input("Which item to remove?: ")
  for row in todo_list:
    if item in row:
      todo_list.remove(row)
  print() 


def main():
  while True:
    time.sleep(1)
    os.system("clear")
    menu = input(f"""
                  🌟Life {newColor("red","Organizer")}🌟

Welcome to the life organizer. Do you want to add, view, edit or remove a to do? > """)
    choose = {
      "add": menuAdd,
      "view": menuView,
      "edit": menuEdit,
      "remove": menuRemove
    }
    choose[menu]()


main()
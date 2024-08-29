# day35_100 days - master todo list

import time
import os

todoList = []

def newColor(color, word):
  if color == "red":
    return f"\033[31m{word}\033[0m"
  elif color == "green":
    return f"\033[32m{word}\033[0m"
  elif color == "blue":
    return f"\033[34m{word}\033[0m"
  elif color == "yellow":
   return f"\033[33m{word}\033[0m"
  elif color == "purple":
   return f"\033[35m{word}\033[0m"
  else:
   return f"\033[0m{word}\033[0m"

def printList():
  print()
  print("✅ To Do List ✅")
  for item in todoList:
    print(item)
  print() 

while True:
  time.sleep(1)
  os.system("clear")

  menu = input(f"""
                To Do List Manager:

Do you want to view, add, edit, or remove an item from the to do list? you can also "erase" the entire list
         """)
  
  if menu == "add":
    item = input("What do you need to do? 👀: ")
    if item in todoList:
      print("item already there")
    else:
      todoList.append(item)
      print("added!")
  elif menu == "view":
    printList()
    while True:
      leaveq = input("press q to quit ⛔: ")
      if leaveq == "q":
        break
  elif menu == "edit":
    item = input("Which item do you want to edit? ✔️: ")
    if item in todoList:
      todoList.remove(item)
      item = input("enter the new value: ")
      todoList.append(item)
      print("edited!")
    else:
      print(f"{item} was not in the to do list 🤨")
  elif menu == "remove":
    item = input("Which item do you want to delete? ⚔️: ")
    if item in todoList:
      sure = input(f"you are about to delete > {item} <  do you want to procceed? y/n: ")
      if sure == "y":
        todoList.remove(item)
        print("item removed")
      else:
        print("returning...")
    else:
      print(f"{item} was not in the to do list 🤨")
  elif menu == "erase":
    sure = input("you are about to delete > ALL THE LIST <  do you want to procceed? y/n: ")
    if sure == "y":
      del todoList
      todoList = []
      print("list purged!")
    else:
      print("returning...")
  else:
    print("invalid option")

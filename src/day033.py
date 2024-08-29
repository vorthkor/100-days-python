# day 33_100 days - to do list manager

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
                ✅  {newColor("yellow","To Do List Manager")}  ✅
                  
  Do you want to {newColor("red","view, add or edit")} your to do list?: """)
  if menu == "add":
    item = input("What do you need to do? 👀: ")
    todoList.append(item)
  if menu == "view":
    printList()
    while True:
      leaveq = input("press q to quit ⛔: ")
      if leaveq == "q":
        break
  elif menu == "edit":
    item = input("Which item have you completed? ✔️: ")
    if item in todoList:
      todoList.remove(item)
    else:
      print(f"{item} was not in the to do list 🤨")
  
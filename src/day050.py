# Day50_100 - ideas

import random, os, time

f = open("ideas.txt", "w")
f.write("")


def add():
  idea = input("Input your idea. > ")
  f = open("ideas.txt", "a+")
  f.write(f"{idea}\n")
  print("Nice! Your idea has been stored.")
  time.sleep(1)


def see():
  f = open("ideas.txt", "r")
  ideas = f.read().split("\n")
  print(random.choice(ideas))
  back = input("\npress any key to return")
  time.sleep(1)
  
  
def main():
  while True:
    os.system("clear")
    print("🌟Idea Storage🌟")
    option = input("Add an idea or see a random idea? a/r. > ")
    os.system("clear")
    if option == "a":
      add()
    else:
      see()
    time.sleep(1)


main()

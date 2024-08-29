# day44_100 - MASTER BINGO

import random

print("♠️♠️♠️ BINGO ♠️♠️♠️")
print()

numbers = []


def rands():
  number = random.randint(1,90)
  return number


def bingoPrint(bingo_numbers):
  print()
  for row in bingo_numbers:
    for item in row:
      print(f"{item:^10}", end=" | ")
    print()
  print()


def createCard():
  bingo_numbers = []
  row = []
  nms = 0
  for steps in range(9):
    numbers.append(rands())
  numbers.sort()
  for elems in range(3):
    row = [numbers[nms],numbers[nms+1],numbers[nms+2]]
    bingo_numbers.append(row)
    nms += 3
  bingo_numbers[1][1] = "BNG"
  return bingo_numbers


def main():
  bingo = createCard()

  x_n = 0
  won = 0
  while won == 0:
    bingoPrint(bingo)
    choose_number = int(input("Next Number: "))
    for f_count, row in enumerate(bingo):
      for count, item in enumerate(row):
        if item == choose_number:
          bingo[f_count][count] = "X"
          x_n += 1
        if x_n == 8:
          won = 1

  print("You have won")
          

main()
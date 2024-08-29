# day43_100 - BINGO!

import random

print("♠️♠️♠️ BINGO ♠️♠️♠️")
print()

bingo_numbers = []
numbers = []

def rands():
  number = random.randint(1,90)
  return number

def bingoPrint(bingo_numbers):
  for row in bingo_numbers:
    print(row)
  

def main():
  for steps in range(8):
    numbers.append(rands())
  
  numbers.sort()
  
  bingo_numbers = [ [ numbers[0] , numbers[1], numbers[2] ] ,
                    [ numbers[3], "BINGO", numbers[4] ],
                    [ numbers[5], numbers[6], numbers[7] ] ]
  bingoPrint(bingo_numbers)

main()
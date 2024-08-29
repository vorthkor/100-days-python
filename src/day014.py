# day 14_100 days - rock paper scissorsss

from getpass import getpass as input

print(3*"*"," 🪨 📄 ✂️ ULTIMATE BATTLE 🪨 📄 ✂️ ",3*"*")
print(42*"-")
print()

print("And... GO!")
print()

player_1 = input("Make your move (R - P - S) > ")
print()
player_2 = input("Choose your fighter (R - P - S) > ")
print()

result_0 = "IT's a TIE 👔 play again!"
result_1 = " Player 1 is the winner!!!!! 🏆"
result_2 = " Player 2 is the winner!!!!! 🏆"

rock_w = " Rock beats Scisscors! 🪨  ✂️ "
paper_w = " Paper beats rock! 📄 🪨 "
scissors_w = " Scissors beats paper! ✂️ 📄 "

if player_1 == "R":
  if player_2 == "R":
    print(result_0)
  elif player_2 == "P":
    print(result_2, paper_w)
  else:
    print(result_1, rock_w)
    
elif player_1 == "P":
  if player_2 == "R":
    print(result_1, paper_w)
  elif player_2 == "P":
    print(result_0)
  else:
    print(result_2, scissors_w)
    
else:
  if player_2 == "R":
    print(result_2, rock_w)
  elif player_2 == "P":
    print(result_1, scissors_w)
  else:
    print(result_0)
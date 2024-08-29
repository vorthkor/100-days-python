# day17_100 days - rock paper scissors loop

from getpass import getpass as input

print(3*"*"," 🪨 📄 ✂️ ULTIMATE BATTLE 🪨 📄 ✂️ ",3*"*")
print(42*"-")
print()

print("And... GO!")
print()

# ********** PHRASES **********

result_0 = "IT's a TIE 👔 play again! \n"
result_1 = " Point to Player 1!"
result_2 = " Point to Player 2!"

result_1_final = " Player 1 is the winner!!!!! 🏆"
result_2_final = " Player 2 is the winner!!!!! 🏆"

rock_w = " Rock beats Scisscors! 🪨  ✂️ "
paper_w = " Paper beats rock! 📄 🪨 "
scissors_w = " Scissors beats paper! ✂️ 📄 "

# ********** VARIABLES **********

player_1_score = 0

player_2_score = 0

# ********** MAIN **********

while True:
  print(3*"-'")
  print(f"The score is player 1: {player_1_score} | versus player 2: {player_2_score}")
  print()

  player_1 = input("Make your move (R - P - S) > ")
  print()
  player_2 = input("Choose your fighter (R - P - S) > ")
  print()
    
  if player_1 == "R":
    if player_2 == "R":
      print(result_0)
    elif player_2 == "P":
      print(result_2, paper_w)
      player_2_score += 1
    else:
      print(result_1, rock_w)
      player_1_score += 1
      
  elif player_1 == "P":
    if player_2 == "R":
      print(result_1, paper_w)
      player_1_score += 1
    elif player_2 == "P":
      print(result_0)
    else:
      print(result_2, scissors_w)
      player_2_score += 1
      
  else:
    if player_2 == "R":
      print(result_2, rock_w)
      player_2_score += 1
    elif player_2 == "P":
      print(result_1, scissors_w)
      player_1_score += 1
    else:
      print(result_0)
  if player_1_score == 3 or player_2_score == 3:
    break
  else:
    continue

print()
if player_1_score == 3:
  print(result_1_final)
else:
  print(result_2_final)

print()
exit()
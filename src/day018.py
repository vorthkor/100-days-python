# day18_100 days - guess numbah

print("""
*****************************************
* GUESS THE NUMBER - ONE-MILLION-TO-ONE *
*****************************************
""")

number = 3012
attempts = 0

while True:
  guess = float(input("What is your guess?: "))
  if guess > number:
    print("Too High 🧐")
    attempts += 1
  elif guess < number and guess >= 0:
    print("Too Low 😭")
    attempts += 1
    continue
  elif guess < 0:
    print("no negative numbers! 🎃 end of game!")
    exit()
  else:
    attempts += 1
    break

print(f"You got it! With only {attempts} guesses! 😎")
    
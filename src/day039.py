# day39_100 days - HANGMAANNN

import random

lives = 6
won = 0
lettersOn = 0
words = []

listOfWords = ["british", "suave", "integrity", "accent", "evil", "genius", "downton"]

wordChosen = random.choice(listOfWords)

wClen = len(wordChosen)

print("🌟Hangman🌟")

while lives > 0 or won == 0:
  letterChosen = input("\nChoose a letter: ").strip().lower()
  
  if letterChosen in wordChosen:
    print("\nCorrect!")
    if letterChosen not in words:
      words.append(letterChosen)
    else:
      print("\nletter already chosen!")
  else:
    print("\nNope, not in there.")
    lives -= 1
    print(f"\n{lives} left.")

  lettersOn = 0

  for letter in wordChosen:
    if letter in words:
      print(letter, end='')
      lettersOn += 1
    else:
      if len(words) == 0:
        print('', end='')
      else:
        print("_", end='')

  if wClen == lettersOn:
    won = 1
    break

if won == 1:
  print(f"\n\nYou won with {lives} lives left.")
else:
  print("\n\nYou lost!")
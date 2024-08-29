# day 21_100 days - math game

print(
  """
  *************
  * MATH GAME *
  *************
  
  """
)

score = 0
good = "Well done! 😎"
bad = "Oh no 🎃 the answer was "

while True:
  mult = int(input("Name your multiples: "))
  print()
  for i in range(1, 11, 1):
    ans = int(input(f"{i} x {mult} = "))
    if ans == (i * mult):
      print(good)
      score += 1
    else:
      print(bad, i*mult)
  print()
  print(f"You scored {score} out of 10!")
  again = input("Play again? y or n > ")
  if again == "y":
    continue
  else:
    break

print("bye!")
exit()
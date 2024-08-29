# day29_100 days - print args

def newColor(color, word):
  if color == "red":
    print("\033[31m", word, sep="", end="")
  elif color == "green":
    print("\033[32m", word, sep="", end="")
  elif color == "blue":
    print("\033[34m", word, sep="", end="")
  elif color == "yellow":
   print("\033[33m", word, sep="", end="")
  elif color == "purple":
   print("\033[35m", word, sep="", end="")
  else:
   print("\033[0m", word, sep="", end="")


print("Super Subroutine")
print("With my ", end="")
newColor("red", "new program ")
newColor("reset","I can just call red('and') ")
newColor("red", "and ")
newColor("reset","that word will appear in the ")
newColor("green", "color ")
newColor("reset","I set it to.")
print("\n\nWith no ", end="")
newColor("blue","weird ")
newColor("yellow","gaps")
newColor("reset",".")
newColor("purple","\n\nEpic")
newColor("reset",".")
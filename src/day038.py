# day38-100 rainbow-ize

red = ["r"]
blue = ["b"]
green = ["g"]
purple = ["p"]
yellow = ["y"]
space = [" "]


# def newColor(color, word):
#   if color == "red":
#     return f"\033[31m{word}\033[0m"
#   elif color == "green":
#     return f"\033[32m{word}\033[0m"
#   elif color == "blue":
#     return f"\033[34m{word}\033[0m"
#   elif color == "yellow":
#    return f"\033[33m{word}\033[0m"
#   elif color == "purple":
#    return f"\033[35m{word}\033[0m"
#   else:
#    return f"\033[0m{word}\033[0m"


myString = input("What sentence do you want rainbow-ising?")
for letter in myString:

  if letter.lower() in red:
    print('\033[31m', end='') #red
  elif letter.lower() in blue:
    print('\033[34m', end='') #blue
  elif letter.lower() in green:
    print('\033[32m', end='') #green
  elif letter.lower() in purple:
    print('\033[35m', end='') #purple
  elif letter.lower() in yellow:
    print('\033[33m', end='') #yellow
  elif letter.lower() in space:
    print('\033[0m', end='') #back to default

  print(letter, end="")
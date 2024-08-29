# day46_100 - dictionariess

# print("👾 MokéBeast - The Non-Copyright Generic Beast Battle Game 👾")

# mokeDeck = {
#   "Name": '',
#   "Type": '',
#   "Move": '',
#   "HP": '',
#   "MP": ''
# }

# for beast in mokeDeck:
#   mokeDeck[beast] = input(f"Input your beast's {beast} > \t").strip().title()

# if mokeDeck["Type"]=="Earth":
#   print("\033[32m", end="")
# elif mokeDeck["Type"]=="Air":
#   print("\033[37m", end="")
# elif mokeDeck["Type"]=="Fire":
#   print("\033[31m", end="")
# elif mokeDeck["Type"]=="Water":
#   print("\033[34m", end="")
# else:
#   print("\033[33m", end="")

# for name, value in mokeDeck.items():
#   if name == "Name":
#     print(f"Your beast is called {value}.") 
#   if name == "Type":
#     print(f"It is an {value} beast") 
#   if name == "Move":
#     print(f"with a special move of {value}")


# for name, value in mokeDeck.items():
#   print(f"{name:<15}: {value}")

john = {"daysCompleted": 46, "streak": 22}
janet = {"daysCompleted": 21, "streak": 21}
erica = {"daysCompleted": 75, "streak": 6}

courseProgress = {"John":john, "Janet":janet, "Erica":erica}

print(courseProgress["Erica"]["daysCompleted"])
# The first bracket contains the key that references the sub dictionary. The second bracket contains the key that references the sub item. This will output '75'.
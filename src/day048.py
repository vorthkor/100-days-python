# day48_100 - files

print("🌟HIGH SCORE TABLE🌟")

while True:

  data = input("Input your initials, score > ").split(",")
  
  f = open("high.score", "a+")

  f.write(f"{data[0]} {data[1]} \n")
  
  # for datas in data:
  #   f.write(f"{datas} ".format(end=""))
  # f.write("\n")

  f.close()
  print("Added to high score table.")
  
  anoth = input("Add another? y/n? ")
  if anoth == "n":
    break

print("bye")
# day7_100-days-band-check

print(6*" ","🧨 Fake fan Finder 🎃")
print(33*"-")
band = input("What is your favorite band? > ")
print("\033[32m",band,"\033[0m")
if band == "Beatles":
  first_album = input("Hum, what was their first album? > ")
  print("\033[32m",first_album,"\033[0m")
  if first_album == "Please please me":
    print("Oh thanks!")
  else:
    print("Oh, I didnt know it!")
else:
  print("Oh, nice then!")
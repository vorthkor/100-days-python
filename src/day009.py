# day 9_100 - my generation

print(3*"*","Generation Identifier",3*"*")
print(33*"-")
print()
year = int(input("Which year were you born? > "))

if year >= 1925 and year <= 1946:
  print("You're a Traditionalist! jelly good!")
elif year >= 1947 and year <= 1964:
  print("Baby Boomer aye? woooo")
elif year >= 1965 and year <= 1981:
  print("Generation X, the X of the question")
elif year >= 1982 and year <= 1995:
  print("Millenial! also generation Y!")
elif year >= 1996 and year <= 2015:
  print("Generation Z, or Zzzzzz")
else:
  print("Well, after Z comes AA on excel, maybe is this...")
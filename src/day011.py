# day 11_100 days - seconds year

print(3*"*","How many seconds are in a year??",3*"*")
print(42*"-")
print()
leap = input("Is this leap year? Y or N: ")
print()

if leap == "N":
  print(365*24*60*60)
else:
  print(366*24*60*60)
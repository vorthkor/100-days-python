# day23_100 days - subroutines



def login():
  while True:
    name = input("What is your username?: ")
    password = input("What is your password?: ")
    if name != "nice" or password != "nice123":
      print("Whoops! I don't recognize that username or password. Try again!")
      continue
    else:
      print("Welcome to Replit!")
      break

  exit()

print("""
  ***********************
  * REPLIT LOGIN SYSTEM *
  ***********************
""")

login()
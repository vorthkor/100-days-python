# day6_100 - login system

print("SECURE LOGIN SYSTEM")
print(33*"+")

username = input("Username > ")
password = input("Password > ")

if username == "mark" and password == "zucks":
  print("Welcome Mark! Welcome to meta")
elif username == "victor" and password == "victao":
  print("Hey there Victor! welcome back!")
elif username == "annd" and password == "anndinhaIncrivel":
  print("Hey there Annd! Welcome back m`luv")
else:
  print("Go away!")
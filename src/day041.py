# day41_100 for on dictionary

print("🌟Website Rating🌟")

name = input("Input the website name: ")

url = input("Input the URL: ")

description = input("Input your a description: ")

rating = input("Input the a star rating out of 5: ")

webRating = {"name": name, "url": url, "description": description, "rating": rating}

for name, value in webRating.items():
  print(f"{name}: {value}")

# name:Replit, URL:replit.com, description:An awesome online IDE, rating:*****

# solution

website = {"name": None, "url": None, "desc": None, "rating": None}

for name in website.keys():
  website[name] = input(f"{name}: ")

print()
for name, value in website.items():
  print(f"{name}: {value}")
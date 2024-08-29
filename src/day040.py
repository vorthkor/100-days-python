# day40_100 - dictionary

print("🌟Contact Card🌟")

user = {"name":"", "birthday":"", "phone":"", "email":"", "address":""}

user["name"] = input("Input your name > ").strip().capitalize()

user["birthday"] = input("Input your date of birth > ").strip()

user["phone"] = input("Input your telephone number > ").strip()

user["email"] = input("Input your email > ")

user["address"] = input("Input your address > ")

print(f'Hi {user["name"]}. Our dictionary says that you were born on {user["birthday"]}, we can call you on {user["phone"]}, email {user["email"]}, or write to {user["address"]}')
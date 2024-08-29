# day37-100 - star wars name generator

print("🌟Star Wars Name Generator🌟")

name = input("Input your first name > ").strip().capitalize()

surname = input("Input your lastname > ").strip().capitalize()

momName = input("Input your mother's maiden name > ").strip().capitalize()

cityName = input("Input the city where you were born > ").strip().capitalize()

starWarsName = f"{name[:3]}{surname[:3].lower()} {momName[:2]}{cityName[-3:]}"

print(f"Your Star Wars name is {starWarsName}")
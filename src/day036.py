# day36_100 - string functions

nameList = []
while True:
  name = input("First Name: ").strip().capitalize()
  surname = input("Last Name: ").strip().capitalize()
  fullName = f"{name} {surname}"
  if fullName not in nameList:
    nameList.append(fullName)
    for names in nameList:
      print(names)
  else:
    print("ERROR: Duplicate name")
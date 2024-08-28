# day 10_100 dyas - tip calculator

print(3*"$", " Tip Calculator",3*"$")
print(33*"-")
print()
myBill = float(input("What was the bill?: "))
perc = int(input("what percentage is the tip?: "))
numberOfPeople = int(input("How many people?: "))
tip_perc = (perc/100) * myBill
answer = (myBill + tip_perc)/ numberOfPeople
print("You all owe", round(answer,2))
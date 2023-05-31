print(12*"*"," Grade Generator ",12*"*")
print(42*"-")
print()

print(
  """
  Letter Grade	Percentage
    A+	        90-100
    A	          80-89
    B	          70-79
    C	          60-69
    D	          50-59
    U	          under 50
  """
)
print(42*"-")
print()

retry = "y"

while retry == "y":
  test = input("Which test did you take? > ")
  print()
  maxScore = int(input("What is the maximum score? > "))
  print()
  points = int(input("How many points did you score? > "))
  print()
  percentage = round((points * 100) / maxScore)
  print()
  if percentage >= 90 and percentage <= 100:
    letterGrade = "A+ 😎"
  elif percentage >= 80 and percentage <= 89:
    letterGrade = "A 🤓"
  elif percentage >= 70 and percentage <= 79:
    letterGrade = "B 🧐"
  elif percentage >= 60 and percentage <= 69:
    letterGrade = "C 😕"
  elif percentage >= 50 and percentage <= 59:
    letterGrade = "D 😟"
  else:
    letterGrade = "U 😭"
  
  print()
  print(12*"*",test," Exam ",12*"*")
  print(42*"-")
  print()
  
  print("Max. Possible Score: ", maxScore)
  print()
  print("Your score: ", points)
  print()
  
  print("You got ", percentage," % which is a ", letterGrade)
  print(42*"-")
  print()

  again = input("Try again? y or n: > ")
  print()

  retry = again

print()
print("bye!")
"""
  PErcentages
  max 50    -----   100%
  points 30 -----    x
  
  
  x = (30 * 100 ) / 50
"""
# day 34_100 days - Email Spam pretty print

import os, time
listOfEmail = []
listOfEmail2 = ["fdnfjknds@vivaldi.net","fdnfjknds@jkudyog.com","fdnfjknds@lim-eng.com","fdnfjknds@buynsell.com.pk","fdnfjknds@staroxalate.com","fdnfjknds@trialseqco-uk.icu","fdnfjknds@tekscans.com","fdnfjknds@vector-kl.com","fdnfjknds@majnandlocal.com","fdnfjknds@gmicaprelam.in"]

def prettyPrint():
  os.system("clear") 
  print("listofEmail") 
  print()
  for index in range(len(listOfEmail)): 
    print(f"{index+1}: {listOfEmail[index]}") 
  time.sleep(1)

def prettySpam():
  os.system("clear")
  for index in range(len(listOfEmail2)):
    print(f"Email {index+1}")
    print(f"Dear {listOfEmail2[index]}")
    print("""
    It has come to our attention that you're missing out on the amazing Replit 100 days of code. We insist you do it right away. If you don't we will pass on your email address to every spammer we've ever encountered and also sign you up to the My Little Pony newsletter, because that's neat. We might just do that anyway.

Love and hugs,
Ian Spammington III""")
    time.sleep(1)
    os.system("clear")

while True:
  print("SPAMMER Inc.")
  menu = input("1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")
  if menu == "1":
    email = input("Email > ")
    listOfEmail.append(email)
  elif menu =="2":
    email = input ("Email > ")
    if email in listOfEmail:
      listOfEmail.remove(email)
  elif menu == "3":
    prettyPrint() 
  elif menu == "4":
    prettySpam()
  time.sleep(1)
  os.system("clear")
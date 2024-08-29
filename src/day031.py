# Day31_100 days - User Interface



def newColor(color, word):
  if color == "red":
    return f"\033[31m{word}\033[0m"
  elif color == "green":
    return f"\033[32m{word}\033[0m"
  elif color == "blue":
    return f"\033[34m{word}\033[0m"
  elif color == "yellow":
   return f"\033[33m{word}\033[0m"
  elif color == "purple":
   return f"\033[35m{word}\033[0m"
  else:
   return f"\033[0m{word}\033[0m"


print(f"""
                {newColor("red","=")}{newColor("white","=")}{newColor("blue","=")} {newColor("yellow","Music App")} {newColor("blue","=")}{newColor("white","=")}{newColor("red","=")}

🔥▶️  Radio Gaga
     {newColor("yellow","Queen")}

PREV
      {newColor("green","NEXT")}
            {newColor("purple","PAUSE")}
""")

print("****************************************")

print(f"""
                  WELCOME TO
             {newColor("blue","--     ARMBOOK     --")}

             {newColor("yellow","Definitely not a rip off of")}
                  {newColor("yellow","a certain other social")}
                        {newColor("yellow","networking site.")}

                  {newColor("red","Honest.")}

                  Username:
                  Password:
""")
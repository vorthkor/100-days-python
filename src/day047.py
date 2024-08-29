# day47_100 - trmpsss

import time, random, os

trumps = {}
trumps["Mr. Morgan"] = {"Intelligence": 89, "Handsomeness": 90, "L33tc0dingskillz": 91, "BaldnessLevel": 92}
trumps["Mr. Colley"] = {"Intelligence": 93, "Handsomeness": 94, "L33tc0dingskillz": 95, "BaldnessLevel": 96}

stats = {"1": "Intelligence",
        "2": "Handsomeness",
        "3": "L33tc0dingskillz",
        "4": "Baldness level"}

players = {"1": "Mr. Morgan",
           "2": "Mr. Colley"}


def main():
  while True:
    time.sleep(2)
    os.system("clear")

    print("""🌟Top Trumps🌟

    Welcome to the Top Trumps 'Most Handsome Computing Teachers' Simulator
    """)
    
    choose = input("Choose your card: 1 - Mr. Morgan  2 - Mr.Colley > ")
    
    stat = input("""
    Choose your stat:
    1. Intelligence
    2. Handsomeness
    3. L33t c0ding skillz
    4. Baldness level > """)

    player = players.get(choose, "invalid")
    statt = stats.get(stat, "invalid")

    print(f"""
    {player} has a {statt} stat of {trumps[player][statt]}\n
    """)

    pc = random.choice(list(trumps.keys()))

    print(f"pc chose {pc}\n")

    if trumps[player][statt] > trumps[pc][statt]:
      print(player, "************* wins! ********")
    elif trumps[player][statt] < trumps[pc][statt]:
      print(pc, "************* wins! ********")
    else:
      print("************* DRAW ********")
    
    again = input("Again? y/n > ")
    if again == "y":
      break
  
  print("bye")


main()

# day26_100 days of code - Music Player

from replit import audio
import os, time

def play():
  time.sleep(6)
  source = audio.play_file('audio.wav')
  source.paused = False # unpause the playback
  control_source = False
  while True:
    os.system("clear")
    print(f"🎵 Now playing: {source.name} 🎵... \n Remaining {source.get_remaining()} ...")
    # Start taking user input and doing something with it
    option_input = int(input("Press 1 -  ⏯️ || Press 2 - ⏪ || Press 0 - ⏹️ \n"))
    if option_input == 1:
      if control_source:
        source.paused = False
        control_source = False
      else:
        source.paused = True
        control_source = True
    elif option_input == 2:
      source.paused = True
      source = audio.play_file('audio.wav')
      source.paused = False # unpause the playback
      control_source = False
    else:
      source.paused = True
      return

while True:
  # clear the screen 
  os.system("clear")

  # Show the menu
  print("""
  🎵🎵🎵 MyPOD Music Player 🎵🎵🎵

  Press 1 to Play
  Press 2 to Exit

  Press anything else to see the menu again.
  """)

  # take user's input
  user_input = int(input("Option: "))

  # check whether you should call the play() subroutine depending on user's input
  if user_input == 1:
    os.system("clear")
    # time.sleep(3)
    play()
  elif user_input == 2:
    os.system("clear")
    time.sleep(3)
    break
  else:
    os.system("clear")
    time.sleep(2)

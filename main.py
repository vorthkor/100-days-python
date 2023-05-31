print(42*"-*")
print(21*"*"," PET SOUNDS ",21*"*")
print(42*"-*")
print()

the_loop = "no"

while the_loop == "no":
  animal = input("What animal do you want?: ")

  if animal == "cow":
    print("A cow goes mooooo 🐮")
    print("""
\|/          (__)    
     `\------(oo)
       ||    (__)
       ||w--||     \|/
   \|/
    """)
    print()
  elif animal == "lemur":
    print("Ummm...the Lesser Spotter Lemur goes awooga.")
    print("""
                 ,,
                ==
               ==
              ==
             ==
             ==
    ,  ,     ==
    |\/|   ,-..-,
  ./(_  \_/      \
      \           |
      | \_,' /^| /
      ( //  /  \ \
      || \ <    \ )
     _\|  \ )   _\\
      ~'  _\|    '~
           '~
    """)
  elif animal == "cat":
    print("The cat goes... meowww 🐶")
    print("""
         ,    ,
        | \--/ |
        ( (0_0)(
         \==Y==/
         /'-"-'>
       _/ < ; (;
      / ,_ |_|_\
snd  ( _,,)\,,),)
     \ '.___
      '-----'
    """)
  elif animal == "dog":
    print("The cat goes... woof woof 🐶")
    print("""
 _   _
/(. .)\    )
  (*)____/|
  /       |
 /   |--\ |
(_)(_)  (_)
    """)
  elif animal == "bat":
    print("The cat goes... lkdnkjadajkdbskajbdajdsjdk")
    print("""
.        _   ,_,   _
.       / `'=) (='` \
.      /.-.-.\ /.-.-.\ 
.jgs   `      "      `
    """)
  
  the_loop = input("Do you want to exit?: ")
  print()

print("bye!!")
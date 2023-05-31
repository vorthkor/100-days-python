# Common Errors

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*

## Name Error
👉 What is the error here?

```python
counter = 0
while true:
  answer = int(input("Enter a number: "))
  print("Adding it up!")
  counter += answer
  print("Current total is", counter)
  addAnother = input("Add another? ")
  if addAnother == "no":
    break
print("Bye!")
```

<details> <summary> 👀 Answer </summary>


`while true` needs to be `while True`. 

Notice when you change the lowercase "t" to a capital "T", the color of the word changes as Replit is now recognizing this as a Boolean loop.


</details>

## Syntax Error
👉 What about this one? What happens when you hit `run`?

```python
counter = 0
while True:
  answer = int(input("Enter a number: "))
  print("Adding it up!")
  counter += answer
  print("Current total is", counter)
addAnother = input("Add another? ")
if addAnother == "no":
  break
print("Bye!")
```

<details> <summary> 👀 Answer </summary>

Notice the error message is saying the syntax error "break outside loop". Do you notice how the last three lines before the bottom `print` statement are *not* a part of the loop as they are not properly indented (look at the vertical lines)? 

Highlight these three lines of code and press `tab` key one time to *indent* this code so it is *inside* the loop.

</details>
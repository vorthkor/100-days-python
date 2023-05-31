# Fix My Code

👉 Try and fix this code which is *full* of errors.

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*

```python
while true:
  color = input("Enter a color: ")
  if color = "red":
  break
  else:
    print("Cool color!")
print("I don't like red")

```

<details> <summary> 👀 Answer </summary>

```python
while True:
  color = input("Enter a color: ")
  if color == "red":
    break
  else:
    print("Cool color!")
print("I don't like red")

```
- The word 'true' needs to be capitalized for a `while True` loop.
- The `if` statement needs `==`.
- There is an indention error with `break`.

</details>
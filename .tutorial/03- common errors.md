# Common Errors

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*

## Name error

👉 Why is this code not working?

```python
def print My Name():
  print("My Name is David")

print My Name()
```
<details> <summary> 👀 Answer </summary>

Just like with variables, you cannot have spaces with subroutines (onlyCamelCase or_using_underscores).

```python
def printMyName():
  print("My Name is David")

printMyName()
```

</details>

## Syntax error

👉 What happens when you `run` this code? Can you spot the error?

```python
def countToFive:
  for i in range(1, 6):
    print(i)

countToFive()
```

<details> <summary> 👀 Answer </summary>

You need to add `()` in the first line, even though there is no argument.

```python
def countToFive():
  for i in range(1, 6):
    print(i)

countToFive()
```

</details>

## What about this one?

👉 Don't be fooled. This error is different than the last example. 

```python
def countToFive():
  for i in range(1, 6):
    print(i)

  countToFive()
```

<details> <summary> 👀 Answer </summary>

When you call your subroutine, make sure it is *NOT* indented.

```python
def countToFive():
  for i in range(1, 6):
    print(i)

countToFive()
```

</details>
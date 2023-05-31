# 👉 Fix My Code

👉 Try and fix this code which is *full* of errors.

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*

```python
counter = 0
while counter < 25:
  print(counter)
  ```
<details> <summary> 👀 Answer </summary>

```python
counter = 0
while counter < 25:
  print(counter)
  counter +=1
  ```
  
</details>

```python
counter = 0
while counter >= 12:
  print(counter)
  counter += 1
```
<details> <summary> 👀 Answer</summary>

```python
counter = 0
while counter <= 12:
  print(counter)
  counter += 1
```

</details>

```python
exit = ""
while exit = "yes":
  print("🥳")
exit = input("Exit?: ")
```
<details> <summary> 👀 Answer </summary>

```python
exit = ""
while exit != "yes":
  print("🥳")
  exit = input("Exit?: ")
  ```

</details>
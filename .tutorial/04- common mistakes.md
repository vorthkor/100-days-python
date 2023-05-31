# Common Errors

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*

## Infinite Loop

`Run` this code. What happens?
```python
counter = 0
while counter < 10:
  print(counter)
  ```
<details> <summary> 👀 Answer </summary>
  
You see a series of infinite 0s printing over and over. Why? You have created an infinite loop because the counter will always be less than 10 in this case. Manually stop the program and specify `counter +=1`.

```python
counter = 0
while counter < 10:
  print(counter)
  counter += 1
```
</details>

## Nothing happens...
`Run` this code. What goes wrong?

```python
counter = 0
while counter > 6:
  print(counter)
  counter += 1 
```
<details> <summary> 👀 Answer </summary>
  
The issue is the condition. It is the wrong way around. The inequality is saying when the counter is greater than 6 to add one. However, the counter is 0. Therefore, it is not greater than six to start. 

Fix this by sorting out the inequality to `<`.

</details>

## Exit
You can use a `while` loop with text too. In the code below, the while condition is saying "as long as you do not type yes, the computer will type 🥳."  

`Run` this code. What do you see?

```python
exit = ""
while exit != "yes":
  print("🥳")
exit = input("Exit?: ")
```

<details> <summary> 👀 Answer </summary>

Wait! No matter what you type, you get 🥳. Check your indentation. Change the variable that controls the condition *within* the loop itself.

```python
exit = ""
while exit != "yes":
  print("🥳")
  exit = input("Exit?: ")
```



</details>
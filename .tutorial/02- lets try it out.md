# Let's try it out

The first number in this range, 100, is the starting value. The second number in this range, 110, is the ending value (Remember to always put the ending number as *one more* than where you want to end up).

👉 What number will the code run first? What number will be last? `Run` the code and find out. 

```python
for i in range(100, 110):
  print(i)

```
## 

👉 What do you expect to print with the range below? `Run` and find out.

```python
for i in range(1, 7):
  print("Day", i)
```
Did you notice that the counter stopped at 'Day 6'? Change the ending value to be *one more* than the last number you want shown---in this case, 8 because we want to display *7* days of the week.

```python
for i in range(1, 8):
  print("Day", i)
```
## 

👉 What happens when you `run` this code?

```python
print("Thirteen Times Table")
for i in range(1, 13):
  print(i, "x 13 =", i * 13)
  ```
  
### Let's add increments to our range.

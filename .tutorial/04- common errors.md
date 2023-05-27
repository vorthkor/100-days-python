# Common Errors


*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*

##

```python
for i in range (10, 0):
  print(i)
```
<details> <summary> 👀 Answer</summary>
  
The third value in the `range` function, increment, is missing. We need to add an increment of `-1` to go backward. Without the increment written, the computer does the default of +1. 

Without the increment listed, we are telling the computer: "start at 10, keep going until 0, and add one each time." This can't be done so nothing will run unless we add an increment.

```python
for i in range (10, 0, -1):
```

</details>
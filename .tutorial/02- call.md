# Call the Subroutine


Calling the subroutine means telling it to run.

👉 We need to 'call' the code by adding one more line to our code with the name of the subroutine and the empty `()`:


```python
def rollDice():
  import random
  dice = random.randint(1, 6)
  print("You rolled", dice)

rollDice()
  ```

*Note that when you call the subroutine, you need to ensure you do NOT indent.*

I can even add a range and roll the dice 100 times by adding this code:

```python
for i in range(100):
  rollDice()
```
### 👉 Try it out for yourself!


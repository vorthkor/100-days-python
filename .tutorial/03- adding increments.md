# Increments

We know that this range will start at 0 and continue to 999,999 (which is the number right *before* the ending value written). The number will increase in increments of 25 each time. 

👉 What numbers do you expect to see? Hit `run` and find out.

```python
for i in range (0, 1000000, 25):
  print(i)
  ```

## Counting Backward

In this example, we are starting at 10 and counting backward to 0 (because 0 is what comes right *before* the ending value listed), and counting backward 1 each time.

👉 What do you expect to see when you hit `run`?

```python
for i in range(10, -1, -1):
  print(i)
```
# 👉 Day 18 Challenge

We are going to build a "Guess the Number" guessing game.

You are going to use a `while` loop and some of the concepts from the past few days.

1. Start by picking a number between 0 and 1,000,000. This will be your first variable.
<details> <summary>💡 Hint </summary> Essentially, what do you want the correct number to be. Create a variable for that number. </details>

2. Create a `while` loop to keep asking the user to guess your number.

3. If they are too low, tell them "too low." If they guess too high tell, them "too high."
<details> <summary> 💡 Hint </summary>

You will need to include `if` statements here with logical operators. Include the correct number variable you created at the beginning in these `if` statements.
</details>

4. If the user guesses correctly, tell them they are a winner (maybe add a fun emoji too!)
<details> <summary> 💡 Hint </summary>

If they are a winner, they need to get out of the loop. How do you do that?
</details>

5. Count the number of attempts it took for the user to guess number. Make sure you only show that *after* they get the answer correct.

<details> <summary> 💡 Hint </summary>

Create a counter *before* the `while` loop and `print` the number of attempts *after* the user is a winner. Don't forget to count attempts using `+=` in the loop.
</details>

Extra challenge: If the user types a negative number, exit program.
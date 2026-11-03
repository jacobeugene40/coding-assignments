# M17 Lesson 5 - Activity 1: Dice Roll
# Run in the VS Code integrated terminal (uses input()).
import numpy as np

die_sides = int(input("enter number of sides for dice (6/12) : "))
die = range(1, die_sides + 1)   # +1 so the top face can be rolled

num_rolls = int(input("Enter number of times you want to roll the dice : "))

results = np.random.choice(die, size=num_rolls, replace=True)
print(results)

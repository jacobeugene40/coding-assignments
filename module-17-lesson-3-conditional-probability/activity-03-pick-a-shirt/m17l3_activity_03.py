# M17 Lesson 3 - Activity 3: Pick a Shirt (with replacement)
# Run in the VS Code integrated terminal (uses input()).

RS = int(input("Enter number of red shirts: "))
BS = int(input("Enter number of blue shirts: "))
WS = int(input("Enter number of white shirts: "))

total = RS + BS + WS

prob_a = BS / total   # 1st shirt blue
prob_b = RS / total   # 2nd shirt red

prob_bga = prob_b     # replaced, so independent
prob_a_and_b = prob_a * prob_b

print("Probability that the second shirt is red given that the first shirt is blue: ")
print(round(prob_bga, 3))

print("Probability that the second shirt is red and the first shirt is blue: ")
print(round(prob_a_and_b, 3))

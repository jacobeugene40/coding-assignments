# M17 Lesson 4 - Activity 1: Strep Throat Part 1
# Run in the VS Code integrated terminal (uses input()).

def find_prob(a, b):
    if a == 1:
        prob_a = 0.2
        prob_bga = {1: 0.85, 2: 0.15}.get(b)
    elif a == 2:
        prob_a = 0.8
        prob_bga = {1: 0.02, 2: 0.98}.get(b)
    else:
        print("Invalid Choice")
        return

    if prob_bga is None:
        print("Invalid Choice")
        return

    print("Probability of b given a:", prob_bga)
    print("Probability of both the events occuring:", round(prob_a * prob_bga, 4))

print("Let's calculate probability. Please enter choices for the events...")

print("Person has strep throat? \n 1. Yes \n 2. No")
a = int(input("Enter your choice (1/2): "))

print("Person has tested positive? \n 1. Yes \n 2. No")
b = int(input("Enter your choice (1/2): "))

print("Probabilities for event a and b:")
find_prob(a, b)

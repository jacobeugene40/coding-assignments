# M17 Lesson 3 - Activity 2: Multiplication Rule
# P(A and B) = P(A) * P(B given A)   (no replacement)
# Run in the VS Code integrated terminal (uses input()).

def prob_a_and_b(orange, blue, total):
    prob_a = orange / total            # 1st ball orange
    prob_bga = blue / (total - 1)      # 2nd ball blue, one ball already removed
    return round(prob_a * prob_bga, 3)

orange = int(input("Enter number of orange balls "))
blue = int(input("Enter number of blue balls "))
total = orange + blue

print('Probability of Getting 1st orange and 2nd blue ball: ')
print(prob_a_and_b(orange, blue, total))

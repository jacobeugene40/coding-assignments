# Print a star pattern using nested for loops
rows = 5

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()
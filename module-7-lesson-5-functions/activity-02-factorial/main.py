# Find the factorial of a number using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

number = int(input("Enter a number: "))
result = factorial(number)

print("The factorial of", number, "is", result)
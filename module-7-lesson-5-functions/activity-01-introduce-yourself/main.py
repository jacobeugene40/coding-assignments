# Function that accepts a name as a parameter and introduces the user
def introduce(name):
    print("Hello! My name is", name + ". Nice to meet you!")

# Take the name as input from the user
user_name = input("Enter your name: ")

# Call the function with the name
introduce(user_name)
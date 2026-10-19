# M8 Lesson 1 - Data Structures in Python - Activity 1: Operations on List

# STEP 1 - Create a list of classmates and print it
classmates = ["Chidi", "Amara", "Tunde", "Ngozi", "Emeka"]
print("Classmates:", classmates)

# STEP 2 - Length, first, last and slicing
print("Total classmates:", len(classmates))
print("First classmate:", classmates[0])
print("Last classmate:", classmates[-1])
print("First three classmates:", classmates[:3])

# STEP 3 - Add, remove, sort (and reverse), printing after each change
classmates.append("Fatima")          # a new student joined
print("After append:", classmates)

classmates.remove("Tunde")           # a student moved schools
print("After remove:", classmates)

classmates.sort()                    # alphabetical order
print("After sort:", classmates)

classmates.reverse()                 # reverse the order
print("After reverse:", classmates)

# STEP 4 - Teacher dictionary
teacher = {
    "name": "Mrs. Adeyemi",
    "subject": "Mathematics",
    "experience": 8
}
print("Teacher:", teacher)

# STEP 5 - Access, update, add, pop
print("Subject:", teacher["subject"])
print("Experience:", teacher.get("experience", "Not found"))

teacher["experience"] = 9                    # update value
teacher["email"] = "adeyemi@school.com"      # add new key
print("After update and add:", teacher)

removed = teacher.pop("experience")          # remove a key
print("Removed experience:", removed)
print("Final teacher dictionary:", teacher)

# STEP 6 - Combine two lists into a student directory with zip()
roll_numbers = [1, 2, 3, 4, 5]
names = ["Amara", "Chidi", "Emeka", "Fatima", "Ngozi"]
directory = dict(zip(roll_numbers, names))
print("Student directory:", directory)
print("Student at roll number 3:", directory[3])
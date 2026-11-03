# M17 Lesson 2 - Activity 2: Intersection of Set
set1 = {'A', 'B', 'C', 'D', 'E'}
set2 = {'B', 'D', 'V', 'X', 'Y', 'Z'}

common = set1.intersection(set2)
total_guests = sorted(common)

print("Total guests to be invited in party are :", len(total_guests))
print("Guest List :", total_guests)

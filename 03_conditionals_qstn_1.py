# 1. Write a program that checks a user's age and prints whether they are a "Minor", "Adult", or "Senior" (65+).

age = 65

if age < 0:
    print("Invalid age")
elif age < 18:
    print("Minor")
elif age < 65:
    print("Adult")
else:
    print("Senior")
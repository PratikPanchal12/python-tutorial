# Grade Checker Program

# Taking score as input
score = int(input("Enter your score: "))

# Checking grade
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

# Printing the grade
print("Your grade is:", grade)

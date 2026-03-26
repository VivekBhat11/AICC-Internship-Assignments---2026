"""

Assignment - 19/02/2026 
Assignment Name : Student Data Manager
Description : Store data for 5 students using dictionaries, print topper, class average, and assign grades.

This program stores data for 5 students using a dictionary, where names are keys and marks are values. It finds the topper by identifying the student with the highest marks and calculates the class average. A function is used to assign grades based on marks. This assignment helps in understanding dictionaries, loops, functions, and basic data analysis in Python.

"""


students = {}

# Input data for 5 students
for i in range(5):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

# Find topper
topper = max(students, key=students.get)

# Calculate average
average = sum(students.values()) / len(students)

# Function to assign grade
def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "D"

# Print results
print("\nTopper:", topper, "-", students[topper])
print("Class Average:", average)

print("\nStudent Grades:")
for name, marks in students.items():
    print(name, ":", marks, "-", get_grade(marks))
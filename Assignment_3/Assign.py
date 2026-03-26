"""
Assignment (12/02/2026)

This program takes user input such as name, age, and hobby. It uses conditional statements to categorize the user into different age groups like child, teenager, adult, or senior. Based on the inputs, it prints a personalized message. This assignment helps in understanding input handling, type conversion, and decision-making using if-else in Python.

"""

name = input("Enter your name: ")
age = int(input("Enter your age: "))
hobby = input("Enter your hobby: ")

# Categorizing age
if age < 13:
    category = "Child"
elif age < 20:
    category = "Teenager"
elif age < 60:
    category = "Adult"
else:
    category = "Senior"

# Personalized message
print("\nHello", name + "!")
print("You are a", category + ".")
print("It's great that you enjoy", hobby + "!")
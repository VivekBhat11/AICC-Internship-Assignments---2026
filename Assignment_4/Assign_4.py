"""

Assignment - 17/02/2026 
Assignment Name : Logic Builder
Description : Print numbers 1–50 with Fizz/Buzz logic and count occurrences using loops and functions.

This program prints numbers from 1 to 50 using a loop. It replaces numbers divisible by 3 with “Fizz”, numbers divisible by 5 with “Buzz”, and numbers divisible by both with “FizzBuzz”. A function is used to organize the logic, and counters are maintained to track how many times each case occurs. This helps in understanding loops, functions, and conditional statements in Python.

"""

def fizz_buzz():
    fizz_count = 0
    buzz_count = 0
    fizzbuzz_count = 0

    for i in range(1, 51):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
            fizzbuzz_count += 1
        elif i % 3 == 0:
            print("Fizz")
            fizz_count += 1
        elif i % 5 == 0:
            print("Buzz")
            buzz_count += 1
        else:
            print(i)

    print("\nCounts:")
    print("Fizz:", fizz_count)
    print("Buzz:", buzz_count)
    print("FizzBuzz:", fizzbuzz_count)

# call function
fizz_buzz()
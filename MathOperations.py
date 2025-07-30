# Day25-MathOperations.py
# This program provides functions for factorial, power, and square root operations.

import math

# Function to calculate factorial
def calculate_factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    return math.factorial(n)

# Function to calculate power
def calculate_power(base, exponent):
    return pow(base, exponent)

# Function to calculate square root
def calculate_square_root(n):
    if n < 0:
        return "Square root of negative number is imaginary."
    return math.sqrt(n)

# Show menu to user
print("Choose a math operation:")
print("1. Factorial")
print("2. Power")
print("3. Square Root")

choice = input("Enter your choice (1/2/3): ")

# Handle each operation
try:
    if choice == '1':
        number = int(input("Enter a number to find its factorial: "))
        result = calculate_factorial(number)
        print(f"\nFactorial of {number} is: {result}")

    elif choice == '2':
        base = float(input("Enter the base: "))
        exponent = float(input("Enter the exponent: "))
        result = calculate_power(base, exponent)
        print(f"\n{base} raised to the power {exponent} is: {result}")

    elif choice == '3':
        number = float(input("Enter a number to find its square root: "))
        result = calculate_square_root(number)
        print(f"\nSquare root of {number} is: {result:.2f}")

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

except ValueError:
    print("Invalid input. Please enter numeric values only.")

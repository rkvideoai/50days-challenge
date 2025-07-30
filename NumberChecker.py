# Day23-NumberChecker.py
# This program checks if a number is positive, even, and prime using functions.

# Function to check if number is positive
def is_positive(num):
    return num > 0

# Function to check if number is even
def is_even(num):
    return num % 2 == 0

# Function to check if number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Ask user to input a number
try:
    number = int(input("Enter an integer: "))

    # Call each function and display results
    print("\nNumber Check Results:")
    print(f"Is Positive? {'Yes' if is_positive(number) else 'No'}")
    print(f"Is Even?     {'Yes' if is_even(number) else 'No'}")
    print(f"Is Prime?    {'Yes' if is_prime(number) else 'No'}")

except ValueError:
    print("Invalid input. Please enter a valid integer.")

#Day 6/50 - AI Python Challenge
#Number Comparison : Compare two numbers and tell which is larger, smaller, or if they're equal.

def compare_two_numbers():
    # Ask the user to enter the first number
    number1 = float(input("Enter the first number: "))

    # Ask the user to enter the second number
    number2 = float(input("Enter the second number: "))

    # Compare the two numbers
    if number1 > number2:
        print(f"\n{number1} is greater than {number2}.")
    elif number1 < number2:
        print(f"\n{number1} is smaller than {number2}.")
    else:
        print(f"\nBoth numbers are equal: {number1} = {number2}")

# Run the function
compare_two_numbers()


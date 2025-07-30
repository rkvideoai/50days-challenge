# Day26-ListHelper.py
# This program provides helper functions to work with a list of numbers:
# It finds max, min, sum, and average.

# Function to find maximum
def find_max(numbers):
    return max(numbers)

# Function to find minimum
def find_min(numbers):
    return min(numbers)

# Function to calculate sum
def calculate_sum(numbers):
    return sum(numbers)

# Function to calculate average
def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

# Ask user to input numbers separated by commas
input_str = input("Enter a list of numbers separated by commas: ")

try:
    # Convert the input string into a list of floats/integers
    number_list = [float(num.strip()) for num in input_str.split(',')]

    # Apply all helper functions
    maximum = find_max(number_list)
    minimum = find_min(number_list)
    total = calculate_sum(number_list)
    average = calculate_average(number_list)

    # Display the results
    print("\nList Helper Results:")
    print(f"Maximum Value : {maximum}")
    print(f"Minimum Value : {minimum}")
    print(f"Sum           : {total}")
    print(f"Average       : {average:.2f}")

except ValueError:
    print("Invalid input. Please enter only numbers separated by commas.")

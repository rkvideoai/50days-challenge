# Day27-DateFunctions.py
# This program includes:
# 1. A function to check if a year is a leap year.
# 2. A function to calculate age from year of birth.

from datetime import datetime

# Function to check if a year is a leap year
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Function to calculate age based on year of birth
def calculate_age(year_of_birth):
    current_year = datetime.now().year
    return current_year - year_of_birth

# Ask user for year input
try:
    year = int(input("Enter a year to check if it's a leap year: "))
    birth_year = int(input("Enter your year of birth to calculate age: "))

    # Call both functions
    leap_result = "Yes" if is_leap_year(year) else "No"
    age = calculate_age(birth_year)

    # Display results
    print("\nDate Function Results:")
    print(f"Is {year} a leap year? {leap_result}")
    print(f"Your age is: {age} years old")

except ValueError:
    print("Invalid input. Please enter valid years as integers.")

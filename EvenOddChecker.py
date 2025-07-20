#Day 3/50 - AI Python Challenge
#Even or Odd Checker : Check if a number is even or odd, then check a list of numbers.

def check_even_or_odd():
    # Step 1: Check a single number
    number = int(input("Enter a number to check if it's even or odd: "))

    # Use modulus operator to check
    if number % 2 == 0:
        print(f"{number} is Even.")
    else:
        print(f"{number} is Odd.")

    # Step 2: Check a list of numbers
    print("\nNow let's check a list of numbers...")

    # Ask user to input numbers separated by commas
    input_list = input("Enter numbers separated by commas (e.g., 1,2,3,4): ")

    # Convert the input string into a list of integers
    numbers = [int(num.strip()) for num in input_list.split(",")]

    # Loop through the list and check each number
    for num in numbers:
        if num % 2 == 0:
            print(f"{num} is Even")
        else:
            print(f"{num} is Odd")

# Run the function
check_even_or_odd()


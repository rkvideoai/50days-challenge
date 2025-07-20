#Day 9/50 - AI Python Challenge
#Sum Calculator : Find sum of all numbers from 1 to n using a loop.

def sum_from_one_to_n():
    # Ask the user to enter a positive whole number
    n = int(input("Enter a positive number (n): "))

    # Initialize a variable to store the total sum
    total_sum = 0

    # Loop from 1 to n and add each number to total_sum
    for number in range(1, n + 1):
        total_sum += number  # Add current number to total

    # Print the final result
    print(f"\n✅ The sum of numbers from 1 to {n} is: {total_sum}")

# Run the function
sum_from_one_to_n()
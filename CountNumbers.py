#Day 8/50 - AI Python Challenge
#Count Numbers : Count how many positive, negative, and zero numbers are in a list.

def count_numbers():
    # Ask the user to enter numbers separated by commas
    user_input = input("Enter numbers separated by commas: ")

    # Convert input string into a list of numbers
    number_list = [int(num.strip()) for num in user_input.split(',')]

    # Initialize counters
    positive_count = 0
    negative_count = 0
    zero_count = 0

    # Loop through each number and update counts
    for number in number_list:
        if number > 0:
            positive_count += 1
        elif number < 0:
            negative_count += 1
        else:
            zero_count += 1

    # Display results
    print("\n📊 Result:")
    print(f"Positive numbers: {positive_count}")
    print(f"Negative numbers: {negative_count}")
    print(f"Zeroes: {zero_count}")

# Run the function
count_numbers()
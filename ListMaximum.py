#Day 13/50 - AI Python Challenge
#List Maximum : Find the largest number in a list without using max() function.

def find_largest_number():
    # Step 1: Define a list of numbers (you can change these or ask user input)
    numbers = [12, 45, 78, 34, 89, 23, 67]

    # Step 2: Assume the first number is the largest
    largest = numbers[0]

    # Step 3: Loop through the list to compare each number
    for num in numbers:
        if num > largest:
            largest = num  # Update largest if current number is bigger

    # Step 4: Print the largest number
    print("📊 Numbers List:", numbers)
    print(f"✅ The largest number in the list is: {largest}")

# Run the function
find_largest_number()
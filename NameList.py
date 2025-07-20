#Day 10/50 - AI Python Challenge
#Name List : Store 5 names in a list and print them with their lengths.

def print_name_lengths():
    # Step 1: Create an empty list to store 5 names
    names = []

    # Step 2: Use a loop to get 5 names from the user
    for i in range(5):
        name = input(f"Please enter name {i+1}: ")
        names.append(name)  # Add the name to the list

    # Step 3: Loop through the list and print name with its length
    print("\n📋 Name List with Lengths:\n")
    for name in names:
        length = len(name)  # len() gives number of characters in the name
        print(f"Name: {name}, Length: {length} characters")

# Run the function
print_name_lengths()
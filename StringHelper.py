# Day24-StringHelper.py
# This program provides helper functions to manipulate a string.

# Function to capitalize the string
def capitalize_text(text):
    return text.capitalize()

# Function to reverse the string
def reverse_text(text):
    return text[::-1]

# Function to count total characters in the string
def count_characters(text):
    return len(text)

# Ask user to enter a string
user_input = input("Enter a string: ")

# Apply helper functions
capitalized = capitalize_text(user_input)
reversed_str = reverse_text(user_input)
character_count = count_characters(user_input)

# Display results
print("\nString Helper Results:")
print(f"Capitalized     : {capitalized}")
print(f"Reversed        : {reversed_str}")
print(f"Character Count : {character_count}")

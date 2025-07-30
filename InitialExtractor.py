# Day17-InitialExtractor.py
# This program takes a full name and extracts the initials of each word.

def extract_initials(full_name):
    # Remove leading/trailing spaces and split the name into parts
    name_parts = full_name.strip().split()

    # Extract the first character of each part and make it uppercase
    initials = [part[0].upper() for part in name_parts]

    # Join initials with dots
    formatted_initials = '.'.join(initials) + '.'

    return formatted_initials

# Ask user for their full name
user_input = input("Enter your full name: ")

# Get the initials
result = extract_initials(user_input)

# Print the result
print("\nExtracted Initials:")
print(result)

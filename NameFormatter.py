# NameFormatter.py
# This program takes a full name and displays it in different formats.

def format_name(full_name):
    # Split the full name into parts (assuming first and last name)
    parts = full_name.strip().split()

    # If user enters less than 2 parts, we can't format properly
    if len(parts) < 2:
        print("Please enter at least first and last name.")
        return

    first = parts[0]
    last = parts[-1]  # Last name is the last part

    # 1. First Last
    format1 = f"{first} {last}"

    # 2. Last, First
    format2 = f"{last}, {first}"

    # 3. Initial. Last
    format3 = f"{first[0]}. {last}"

    # Print all formats
    print("\nFormatted Name Outputs:")
    print("1. First Last      :", format1)
    print("2. Last, First     :", format2)
    print("3. Initial. Last   :", format3)

# Ask user for full name
user_name = input("Enter your full name (First Last): ")

# Call the formatting function
format_name(user_name)

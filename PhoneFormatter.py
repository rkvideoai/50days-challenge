# Day21-PhoneFormatter.py
# This program formats a 10-digit number as (XXX) XXX-XXXX

def format_phone_number(number):
    # Remove any spaces, dashes, or parentheses from input
    digits = ''.join(filter(str.isdigit, number))

    # Check if we have exactly 10 digits
    if len(digits) != 10:
        return "Error: Please enter exactly 10 digits."

    # Format the number
    formatted = f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
    return formatted

# Ask user to enter a phone number
user_input = input("Enter a 10-digit phone number: ")

# Call the function to format it
result = format_phone_number(user_input)

# Print the formatted number or error
print("\nFormatted Phone Number:")
print(result)

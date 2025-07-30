# Day19-EmailUsername.py
# This program extracts the username (part before '@') from an email address.

def extract_username(email):
    # Use split to separate the email at '@' and take the first part
    if '@' in email:
        username = email.split('@')[0]
        return username
    else:
        return "Invalid email address. Please include '@'."

# Ask user to enter an email address
user_input = input("Enter your email address: ")

# Get the username
result = extract_username(user_input)

# Print the result
print("\nExtracted Username:")
print(result)

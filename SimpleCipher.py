# Day18-SimpleCipher.py
# This program shifts each letter in the input word by 1 position in the alphabet (simple cipher).

def simple_cipher(word):
    result = ""

    for char in word:
        # Check if character is a lowercase letter
        if char.islower():
            # Shift letter and wrap from 'z' to 'a'
            shifted = chr((ord(char) - ord('a') + 1) % 26 + ord('a'))
            result += shifted

        # Check if character is an uppercase letter
        elif char.isupper():
            # Shift letter and wrap from 'Z' to 'A'
            shifted = chr((ord(char) - ord('A') + 1) % 26 + ord('A'))
            result += shifted

        else:
            # Keep digits/symbols unchanged
            result += char

    return result

# Ask user to input a word
user_input = input("Enter a word to cipher: ")

# Get the ciphered result
ciphered_word = simple_cipher(user_input)

# Print the result
print("\nCiphered Output:")
print(ciphered_word)

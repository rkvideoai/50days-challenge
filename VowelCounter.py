# Day14-VowelCounter.py
# This program counts how many vowels are in a given word entered by the user.

def count_vowels(word):
    # Define all vowels (both lowercase and uppercase for flexibility)
    vowels = "aeiouAEIOU"
    
    # Initialize a counter to 0
    count = 0

    # Loop through each letter in the word
    for letter in word:
        if letter in vowels:
            count += 1  # If letter is a vowel, increase the count

    return count  # Return total number of vowels

# Ask user to enter a word
user_input = input("Enter a word to count vowels: ")

# Call the function to count vowels
vowel_count = count_vowels(user_input)

# Print the result
print(f"The word '{user_input}' contains {vowel_count} vowel(s).")

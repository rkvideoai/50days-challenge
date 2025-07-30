# Day20-TextStatistics.py
# This program calculates the number of words, sentences, and characters in a given paragraph.

def text_statistics(text):
    # Count characters (including spaces and punctuation)
    total_characters = len(text)

    # Count words (split by whitespace)
    total_words = len(text.split())

    # Count sentences (ends with '.', '!', or '?')
    sentence_endings = '.!?'
    total_sentences = sum(1 for char in text if char in sentence_endings)

    # Display results
    print("\nText Statistics:")
    print(f"Total Characters : {total_characters}")
    print(f"Total Words      : {total_words}")
    print(f"Total Sentences  : {total_sentences}")

# Ask user to enter a paragraph
user_input = input("Enter a paragraph:\n")

# Call the function
text_statistics(user_input)

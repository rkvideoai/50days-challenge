# Day16-WordReverser.py
# This program takes a sentence and reverses each word individually.

def reverse_words(sentence):
    # Split the sentence into words using space
    words = sentence.split()

    # Reverse each word using slicing [::-1]
    reversed_words = [word[::-1] for word in words]

    # Join the reversed words back into a sentence
    reversed_sentence = ' '.join(reversed_words)

    return reversed_sentence

# Ask user to enter a sentence
user_input = input("Enter a sentence: ")

# Call the function to reverse words
result = reverse_words(user_input)

# Print the result
print("\nReversed Words Sentence:")
print(result)

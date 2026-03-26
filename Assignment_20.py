"""
Assignment (21/03/2026)

Assignment Name : Build a Text Cleaner
Description : Write code to remove punctuation, lowercase text, remove stopwords and test it.


This program cleans text data by converting it to lowercase, removing punctuation, and eliminating common stopwords. The cleaned text is more suitable for natural language processing tasks, as it removes unnecessary words and symbols.

"""

import string

# Sample stopwords list
stopwords = ["is", "the", "and", "a", "an", "in", "on"]

# Input text
text = input("Enter a sentence: ")

# Convert to lowercase
text = text.lower()

# Remove punctuation
text = text.translate(str.maketrans('', '', string.punctuation))

# Remove stopwords
words = text.split()
cleaned_words = [word for word in words if word not in stopwords]

# Final cleaned text
cleaned_text = " ".join(cleaned_words)

print("Cleaned Text:", cleaned_text)
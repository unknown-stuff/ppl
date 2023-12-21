CODE:
import re
def count_words_frequency(text):
word_count = {}
words = re.findall(r'\b\w+\b', text)
for word in words:

word = word.strip(".,!?").lower()
if word:

word_count[word] = word_count.get(word, 0) + 1
return word_count
# Function to demonstrate the use of dictionary functions
def demonstrate_dictionary_functions(text):
word_frequency = count_words_frequency(text)
# Printing the word frequency
for word, frequency in word_frequency.items():
print(f"{word}: {frequency}")
# Using dictionary methods
word_frequency.clear()
print("Cleared dictionary:", word_frequency)
# Example usage
text = "This is a simple example. This is a Python program."
demonstrate_dictionary_functions(text)

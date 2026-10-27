import string

review = """I love Swiggy. I love the food and fast delivery!"""

# Convert text to lowercase
review = review.lower()

# Remove punctuation
for char in string.punctuation:
    review = review.replace(char, "")

# Split the review into words
words = review.split()

# Create an empty dictionary
word_count = {}

# Count word frequency
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word Frequency:", word_count)
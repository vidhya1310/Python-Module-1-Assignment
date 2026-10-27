import string

def word_freq_dict(text):
    text = text.lower()

    # Remove punctuation
    for char in string.punctuation:
        text = text.replace(char, "")

    words = text.split()

    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count


text = "Virat scored 100, Rohit scored 80, and Gill scored 50 in the IPL match"

result = word_freq_dict(text)

print(result)
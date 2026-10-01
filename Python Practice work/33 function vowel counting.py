def count_vowels(s):
    count = 0

    for i in s:
        if i in "aeiouAEIOU":
            count += 1

    return count


s = input("Enter String: ")

result = count_vowels(s)

print("Total Vowels:", result)
l1 = ["maam", "php", "java", "c++"]
l2 = []

for i in l1:
    if i == i[::-1]:
        l2.append(i)

print("Palindrome List:", l2)
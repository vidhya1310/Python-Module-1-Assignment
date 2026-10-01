# """l=[56,32,24,16,21]

# l.sort()

# print("Smallest :",l[0])
# print("Largest :",l[-1])
# print("Second Largest :",l[-2])"""

# #shorting without in built method

# """l = [56, 32, 24, 16, 21]

# largest = l[0]
# second_largest = l[0]
# smallest = l[0]

# for i in l:
#     if i > largest:
#         second_largest = largest
#         largest = i

#     elif i > second_largest:
#         second_largest = i

#     if i < smallest:
#         smallest = i

# print("Smallest :", smallest)
# print("Largest :", largest)
# print("Second Largest :", second_largest)"""

# l = [56, 32, 24, 16, 21]

# largest = []
# second_largest =[]
# smallest = []

# for i in l:
#     if i > largest:
#         second_largest = largest
#         largest=i

#     elif i > second_largest:
#         second_largest = i

#     if i < smallest:
#         smallest = i

# print("Smallest :", smallest)
# print("Largest :", largest)
# print("Second Largest :", second_largest)

# bubble sorting without using built-in function
l = [56, 32, 24, 16, 21]

for i in range(len(l)):
    for j in range(i+1, len(l)): 
        if l[j] < l[i]:
            temp = l[i]
            l[i] = l[j]
            l[j] = temp

print("Sorted List:", l)
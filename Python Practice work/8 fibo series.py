# While loop
"""n = int(input("Enter number of terms: "))

a = 0
b = 1
i = 1

while i < n:
    print(a, end=" ")

    c = a + b
    a = b
    b = c

    i += 1"""

# for loop

n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a,end=" ")
    
    c = a + b
    a = b
    b = c

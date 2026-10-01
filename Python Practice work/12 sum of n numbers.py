"""n=int(input("Enter The Number :"))

sum=0
i=1

while i<=5:
    sum=sum+i
    print(i)
    i+=1

print("Sum =", sum)
"""
# for loop

n = int(input("Enter The Number : "))

sum = 0

for i in range(1, n + 1):
    sum = sum + i
    print(i)

print("Sum =", sum)
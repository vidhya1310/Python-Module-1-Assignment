n = int(input("Enter Number: "))

temp = n
sum = 0

while n > 0:
    digit = n % 10
    sum = sum + digit ** 3
    n //= 10

if sum == temp:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
def armstrong(n,sum=0):
    temp = n
    while n > 0:
        digit = n % 10
        sum = sum + digit ** 3
        n //= 10

    if sum == temp:
        print("Armstrong Number")
    else:
        print("Not Armstrong Number")

    return n

n = int(input("Enter Number: "))

armstrong(n)
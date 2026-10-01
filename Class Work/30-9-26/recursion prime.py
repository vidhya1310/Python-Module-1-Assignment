def prime(n, i=2):

    if n < 2:
        return False

    if i == n:
        return True

    if n % i == 0:
        return False

    else:
        return prime(n, i + 1)


n = int(input("Enter Number: "))

if prime(n):
    print("Prime Number")
else:
    print("Not Prime Number")
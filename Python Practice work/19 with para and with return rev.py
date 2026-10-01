def rev_number(n, rem=0, rev=0):

    for i in range(n):
        if n == 0:
            break

        rem = n % 10
        rev = rev * 10 + rem
        n //= 10

    return rev

n = int(input("Enter Number: "))

result = rev_number(n)

print("Your reverse number :", result)

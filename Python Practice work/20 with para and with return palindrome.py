def palindrome(n):

    num = n
    reverse = 0
    rem = 0

    for i in range(n):
        if n == 0:
            break

        rem = n % 10
        reverse = reverse * 10 + rem
        n //= 10

    if num == reverse:
        print("Palindrome Number")

    else:
        print("Not a Palindrome Number")

n = int(input("Enter Number: "))

palindrome(n)

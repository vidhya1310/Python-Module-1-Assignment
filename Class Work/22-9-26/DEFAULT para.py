"""# default 

def rev_number():
    n=int(input("Enter Number :"))
    rem=0
    rev=0
    while(n!=0):
        rem=n%10
        rev=rev*10+rem
        n//=10
    print(rev)

rev_number()

# with para and arg

def rev_number(n,rem=0,rev=0):

    while(n!=0):
        rem=n%10
        rev=rev*10+rem
        n//=10
    print(rev)

    n=int(input("Enter Number :"))
    rev_number(n)

# without para and with return 

def rev_number():
    n=int(input("Enter Number :"))
    rem=0
    rev=0
    while(n!=0):
        rem=n%10
        rev=rev*10+rem
        n//=10
    print(rev)

    return rev

print(rev_number)"""

# with para and with return

def rev_number(n, rem=0, rev=0):

    while n != 0:
        rem = n % 10
        rev = rev * 10 + rem
        n //= 10

    return rev

n = int(input("Enter Number: "))

result = rev_number(n)

print("Your reverse number :", result)

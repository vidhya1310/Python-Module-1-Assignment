
def fect(n):
    fact=1

    for i in range(1,n+1):
        fact=fact*i
    print("fact number is :",fact)

n = int(input("Enter Number: "))

fect(n)

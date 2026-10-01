def fibo():
    n=int(input("Enter choice :"))
    n1=0
    n2=1

    for i in range(3,n+1):
            n3=n1+n2
            print(n3)
            n1=n2
            n2=n3

def rev_number(n,rem=0,rev=0):

      while(n!=0):
            rem=n%10
            rev=rev*10+rem
            n//=10

            print(rev)

n1=int(input("Enter Number : "))
rev_number(n1)

def rev_number(n,prime=0):

    for i in range(1,n+1):
        if(n%i==0):
            prime+=1

        if(prime==2):
            print("No Is Prime")

        else:
            print("No Not Valid")

n=int(input("enter number"))
print(n)
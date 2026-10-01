while True:
    menu="""
    press 1 for fibo series
    press 2 for prime series
    press 3 for rev series
    press 4 for exit
    """

    print(menu)
    choice=int(input("Enter Choice :"))

    if choice==1:
        n=int(input("Enter choice :"))
        n1=0
        n2=1

        for i in range(3,n+1):
            n3=n1+n2
            print(n3)
            n1=n2
            n2=n3

    elif choice==2:
        n=int(input("enter number"))
        prime=0

        for i in range(1,n+1):
            if(n%i==0):
                prime+=1

            if(prime==2):
                print("No Is Prime")

            else:
                print("No Not Valid")

    elif choice==3:
        n=int(input("enter number"))
        rem=0
        rev=0
        n1=n

        while(n!=0):
            rem=n%10
            rev=rev*10+rem
            n//=10

        print(rev)
 

    elif choice==4:
        print("Exit")
        break

    else:
        print("Invalid Choice!")
        break
# 1. Without Parameter & Without Return Type
def add():
    a = 30
    b = 50
    print("Addition:", a + b)


# 2. With Parameter & Without Return Type
def sub(a, b):
    a=30
    b=20.
    
    print("Subtraction:", a - b)


# 3. Without Parameter & With Return Type
def mul():
    a = 30
    b = 50
    return a * b


# 4. With Parameter & With Return Type
def fact(n):
    factorial = 1

    for i in range(1, n + 1):
        factorial = factorial * i

    return factorial

while True:

    menu="""
    press 1 for addition
    press 2 for substraction
    press 3 for multiplication
    press 4 for fectorial
    press 5 for exit
    """

    print(menu)
    choice=int(input("Enter Choice :"))

    if choice==1:
        def add():
            a=30
            b=50
            return a+b
        print("Addition :",add())

    elif choice==2:
        def sub():
            a=80
            b=50
            return a-b
        print("Substraction :",sub())

    elif choice==3:
        def mul():
            a=30
            b=50
            return a*b
        print("Multiplication :",mul())

    elif choice==4:
        def fect():
            n=3
            fact=2
            return n*fact
        print("Fectorial :",fect())

    elif choice==5:
        print("Exit")
        break

else:
    print("Invalid Choice")
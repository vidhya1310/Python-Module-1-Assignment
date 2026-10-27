# class Myclass:

#     def fun1(self):
#         print("Method !")

# class Myclass1(Myclass):

#     def fun2(self):
#         print("Mrhod 2!")

# obj=Myclass1()
# obj.fun1()
# obj.fun2()

# class Menu:
#     def menu(self):
#         print("Sign Up")

# class menu1(Menu):
#     def menu1(self):
#         print("Sign out")

# obj=menu1()
# obj.menu()
# obj.menu1()

class Fibo:
    def fibo(self,a=0,b=1):
        n = int(input("Enter Terms : "))
        for i in range(n):
            print(a,end=" ")
            c = a + b
            a = b   
            b = c

class Prime(Fibo):
    def prime(self,prime=0):
        n = int(input("Enter Number : "))

        for i in range(1, n + 1):
            if n % i == 0:
                prime+= 1

        if prime == 2:
            print("Prime Number!!")
        else:
            print("Not a Prime Number!!")

class Reverse(Prime):
    def reverse(self):
        n = int(input("Enter Number : "))
        rev = 0

        while n != 0:
            rem = n % 10
            rev = rev * 10 + rem
            n //= 10

        print("Reverse Number :", rev)

obj = Reverse()

while True:

    menu = """
    Press 1 for Fibo Series
    Press 2 for Prime Number
    Press 3 for Rev Number
    Press 4 for Exit
    """

    print(menu)

    choice = int(input("Enter Choice : "))

    if choice == 1:
        obj.fibo()

    elif choice == 2:
        obj.prime()

    elif choice == 3:
        obj.reverse()

    elif choice == 4:
        print("Thank you")
        break

    else:
        print("Invalid Choice")
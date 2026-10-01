"""a=int(input("Enter Number 1 Is :"))
b=int(input("Enter Number 2 Is :"))

if (a>b):
    print("Number Is Grater Than A !")

elif(b>a):
    print("Number Is Grater Than B !")

else:
    print("Both Are Eqal")"""

n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
n3 = int(input("Enter number 3: "))
n4 = int(input("Enter number 4: "))

if n1 > n2 and n1 > n3 and n1 > n4:
    print("Number 1 is greater")

elif n2 > n1 and n2 > n3 and n2 > n4:
    print("Number 2 is greater")

elif n3 > n1 and n3 > n2 and n3 > n4:
    print("Number 3 is greater")

elif n4 > n1 and n4 > n2 and n4 > n3:
    print("Number 4 is greater")

else:
    print("number Not valid !")

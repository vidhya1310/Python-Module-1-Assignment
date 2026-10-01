"""def fun1():
    a=30
    b=50

    return a+b

print("Addition :",fun1())"""

"""def fact():

    n=5
    fact=5

    return n*fact

print("Factorial :",fact())"""

def rev_number(n,rem=0,rev=0):

      while(n!=0):
            rem=n%10
            rev=rev*10+rem
            n//=10

            return rev
      n=int(input("Enter Number"))
      print("Reverse :",rev_number())

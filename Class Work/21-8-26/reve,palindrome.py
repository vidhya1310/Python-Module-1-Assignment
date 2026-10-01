n =int(input("Enter Number :"))
rem=0
rev=0
n1=n

while(n!=0):
    rem = n%10        #5368 =536.8 
    rev=rev*10+rem    #0+6=6 60+3=63
    n//=10            #583  58

#print(rev)

if n1==rev:
    print("Palindrome!")

else:
    print("Not Pallindrome!")
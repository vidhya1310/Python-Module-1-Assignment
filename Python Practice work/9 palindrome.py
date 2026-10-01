"""n = int(input("Enter a number: "))

num = n
reverse = 0
n1=n

while num > 0:
    n1 = num % 10
    reverse = reverse * 10 + n1
    num = num // 10

if n == reverse:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")"""

# for loop

no= int(input("Enter a number: "))
reverse = 0
rem=0
n=no

for i in range(no):
    if no==0:
        break
    rem=no%10
    reverse=reverse*10+rem
    no//=10

if n== reverse:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")
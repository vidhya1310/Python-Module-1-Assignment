n =int(input("Enter Number :"))

prime=0
for i in range(1,n+1):
    if(n%i==0):
        prime+=1

    if(prime==2):
        print("Prime Number")

    else:
        print("Not Prime Number")

# while loop

n= int(input("Enter Number :"))
prime = 0
i = 1

while i <= n:
    if n % i == 0:
        prime += 1

    i += 1

if prime == 2:
    print("Prime Number")
else:
    print("Not Prime Number")
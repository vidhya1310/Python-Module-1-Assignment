i =1

ev=0
od=0
evsum=0
odsum=0
sum=0

while(i<=5):
    n=int(input("Enter Number"))
    if(n%2==0):
        print("Even")
        ev+=1
        evsum+=n

    else:
        print("Odd")
        od+=1
        odsum+=n
    sum+=n    
    i+=1

print("Even Num",ev)
print("Odd Num",od)
print("Even Sum",evsum)
print("Odd Sum",odsum)
print("Total Sum",sum)
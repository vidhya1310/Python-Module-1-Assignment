n=int(input("Enter Number :"))
l = []
ev =[]
od = []

for i in range (1,n+1):
    l.append(i)

    if i%2==0:
        ev.append(i)
    else:
        od.append(i)

print(l)
print(ev)
print(od)

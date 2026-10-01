l=[10,20,30,40,50]

for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        l[j],l[i]=l[i],l[j]

print("Reverse List",l)
#without built in 
l=[20,30,40,50,10,60]

for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[j]<l[i]:
            temp=l[i]
            l[i]=l[j]
            l[j]=temp

print("Shorted List",l)
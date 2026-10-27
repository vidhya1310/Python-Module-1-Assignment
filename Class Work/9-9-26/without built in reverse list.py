
l=[56,62,21,14,11]

for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        l[j],l[i]=l[i],l[j]

print(l)
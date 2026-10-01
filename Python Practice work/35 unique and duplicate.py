l =[40,30,20,20,30,40,50,60]
uni=[]
dup=[]

for i in l:
    if i not in uni:
        uni.append(i)

    else:
        dup.append(i)

print(uni)
print(dup)
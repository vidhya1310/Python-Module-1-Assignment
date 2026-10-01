l=[1,2,3,1,2,4,5]
uni=[]
dup=[]

for i in l:

    if i not in uni:
        uni.append(i)

    else:
        dup.append(i)

print(uni)
print(dup)
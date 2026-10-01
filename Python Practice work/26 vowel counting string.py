s=input("Enter Name :")
count=0
for i in s:
    if i in 'aeiou':
        count+=1

print("voels are:",count)
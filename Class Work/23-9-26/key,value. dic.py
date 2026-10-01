#without built in method list convert into list
l=[6,8,78]
l1=[53,24,26]

d={}

for i in range(len(l)):
    d[l[i]]=l1[i]

print(d)

#sqar and cube

d={}

for i in range(1,31):
    d[i]=i*i*i

print(d)

# name speling count

s=input("Enter name :")
d={}

for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1

print(d)

# addition of same key

d = {'p': 400, 'q': 200, 'r': 250}
d1 = {'p': 200, 'q': 100}

ans = {}

for i, j in d.items():
    for k, l in d1.items():

        if i == k:
            ans[i] = j + l

        if i not in ans:
            ans[i]=j

print(ans)
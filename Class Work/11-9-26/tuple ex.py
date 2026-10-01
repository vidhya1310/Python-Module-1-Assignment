# t1 = (1,2,"a","b",1.5,2.5)
# l=list(t1)
# print(l)
# print(type(t1))

# print(t1.count(1))

# print(t1.index(2))

#tupple converting list

t1 = (1,2,"a","b",1.5,2.5)
l=list(t1)
print(l)

l.append(100)
t1=tuple(l)
print(t1)
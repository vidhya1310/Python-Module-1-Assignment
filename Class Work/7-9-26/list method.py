l=[10,20,10,7 , True,"Hello",1,1]

print(type(l))

l.append(100) #last me add hoga
print(l)

print(l.count(l)) #count of 1

l.extend([600,800,1000]) #last me add hoga multiple data
print(l)

l.insert(2,"Python") #2nd index me add hoga
print(l)

l.pop() #last index remove karega
print(l)

l.pop(2)
print(l)

l.remove(1) #last ka remove karega position wise
print(l)

l.clear()#clear karega
print(l)

l=[1,4,5,3]

l.sort()
print(l)
d = {1:"hello",2:"python",3:"best"}

print(d)
print(d.copy)#copy value
print(d.get(2))#get value
print(d.items())#show all key value
print(d.keys)#keys ko print karegi
print(d.values())#print values
d.update({4:"why",5:"me"}) #dic add karega
print(d)
d.pop(2)#remove specific key
print(d)

d.popitem()#Removes the last key-value p0ir
print(d)

t=(1,2,3)
d1={}
print(d1.fromkeys(t,"20"))
calls=(12,5,0,20,7,3,15)

l=list(calls)

for call in l.copy():
    if call<5:
        l.remove(call)
        
calls=tuple(l)
print(calls)
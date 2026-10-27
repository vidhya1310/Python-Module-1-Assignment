# file = open("task1.txt","w")
# file.write("write here !")
# file.close()

# file = open("task1.txt","a")
# file.write("write here !")
# file.close()

# file = open("task1.txt","r")
# print(file.read())
# file.close()

# l=[]

# for i in range(1,11):
#     l.append(i)
# file = open("task2.txt","w")
# file.write(str(l))
# file.close()

#write read

# file = open("task3.txt","w+")
# file.write("w+ is here !")
# print(file.tell())
# file.seek(0)
# print(file.read())
# file.close()

# read

file = open("task3.txt","r+")
file.write("r+ is here !")
print(file.tell())      
file.seek(0)
print(file.read())
file.close()
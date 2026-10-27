# class user:
#     def __init__(self,a,b):
#         print("Init Called!")
#         self.a=a
#         self.b=b

#     def __str__(self):
#         return f"{self.a},{self.b}"

#     def __add__(self,obj):
#         x = self.a+obj.a
#         y = self.b+obj.b

#         return(x,y)

# obj=user(10,20)
# print(obj)

# obj1=user(50,60)
# print(obj1)

# print("Addition Is : ",obj+obj1)

class user:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __mul__(self,obj):
        x = self.a-obj.a
        y = self.b-obj.b

        return(x,y)

obj=user(50,60)
print(obj)

obj1=user(30,20)
print(obj1)

print("Subtraction Is : ",obj-obj1)
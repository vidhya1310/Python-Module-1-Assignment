# class Override:

#     def fun1(self):
#         print("Mehod 1")

# class Override1(Override):

#     def fun1(self):
#         super().fun1()
#         print("Method 2")

# obj=Override1()
# obj.fun1()

class a:
    def fun1(self):
        print("Mehod 1!")

class b:
    def fun1(self):
        super().fun1()
        print("Method 2!")

class c(b,a):
    def fun1(self):
        super().fun1()
        print("Mehod 3!")

obj=c()
obj.fun1()

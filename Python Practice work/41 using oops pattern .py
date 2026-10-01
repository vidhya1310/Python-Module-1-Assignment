# right angle
class pattern:
    def right():
        for i in range(1,6):
            print(" *"*i)
    def left():
        for i in range(1,6):
            print("  "*(6-i)," *"*i)
    def triangle():
        for i in range(1,6):
             print(" "*(6-i)," *"*i)
    def sqare():
        for i in range(5):
           print("* " *5)

    def diamond():
        for i in range(1,6):
            for k in range(1,6-i):
                print(" ",end="")

            for j in range(1,i+1):
                print("*",end=" ")

            print()

        for i in range(4,0,-1):
            for k in range(1,6-i):
                print(" ",end="")
            for j in range(1,i+1):
                print("*",end=" ")
                
            print()
p=pattern
p.right()
p.left()
p.triangle()
p.sqare()
p.diamond()


# class left_patern:
#     def left(self):
#         for i in range(1,6):
#             print("  "*(6-i)," *"*i)
# p=left_patern()
# p.left()

# triangle angel

# class traingle_patern:
#     def triangle(self):
#         for i in range(1,6):
#             print(" "*(6-i)," *"*i)
# p=traingle_patern()
# p.traiangle()

# sqare patern

# class sqare:
#     def sqare(self,n):
#         for i in range(n):
#             print("* " * n)
# p=sqare()
# p.sqare(5)

# diamond
# class diamond_patern:
#     def diamond():
#         for i in range(1,6):

#             for k in range(1,6-i):
#                 print(" ",end="")

#             for j in range(1,i+1):
#                 print("*",end=" ")

#             print()

#         for i in range(4,0,-1):
#             for k in range(1,6-i):
#                 print(" ",end="")
#             for j in range(1,i+1):
#                 print("*",end=" ")
                
#             print()

# p=diamond_patern
# p.diamond()
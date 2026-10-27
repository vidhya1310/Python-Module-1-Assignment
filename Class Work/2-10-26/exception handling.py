# try:
#     n=int(input("Enter a number:"))

#     if n==0:
#         print("Zero")
#     else:
#         print("Not Zero")

# except ValueError as e:
#     print("e")

# else:
#     print("try here")
# finally:    
#     print("everytime")

# value error
# zero

# try:
#     n=int(input("Enter a number 1:"))
#     n1=int(input("Enter a number 2:"))

#     print("Division is ",n/n1)

# except ValueError as e:
#     print("e")
# except ZeroDivisionError as e:
#     print("e")

try:
    l=[78,54,21,16,11]

    n=int(input("Enter a number 1:"))

    print("Value of Index is ",l[n])

except Exception as e:
    print(e)
    print("Invalid Input !")
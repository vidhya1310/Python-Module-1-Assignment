s=(input("Enter Name :"))

rev=s[::-1]

if s==rev[::-1]:
    print("Palindrome")

else:
    print("Not palindrome")
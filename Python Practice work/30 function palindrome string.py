def palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

s=input("enter name :")

result=palindrome(s)

if result:
    print("Palindrome ")
else:
    print("Not Palindrome")
def middle(s):

    if len(s)%2==0:
        return s
    else:
        mid=len(s)//2
        return s[mid-1]+s[mid]+s[mid-1]

s=input("Enter Name :")

result = middle(s)

print(result)
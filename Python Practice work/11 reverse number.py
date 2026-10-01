no = int(input("Enter a number: "))

reverse = 0

while num > 0:
    no = num % 10
    reverse = reverse * 10 + no
    num //= 10

print("Your Reverse Number Is :", reverse)
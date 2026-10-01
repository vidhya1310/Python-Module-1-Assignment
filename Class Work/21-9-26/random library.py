import random

lucky = random.randint(1,50)
print(lucky)
while True:
    print("********* Enter Number Between 1 To 50 *********")

    choice = int(input("Enter Number :"))

    if choice>50:
        print("Invalid Number !!")
        break

    elif choice==lucky:
        print("Congrats You Win This!!")
        break

    elif lucky>choice:
        print("Original Number is bigger")

    else:
        print("Original Number Is smaller")

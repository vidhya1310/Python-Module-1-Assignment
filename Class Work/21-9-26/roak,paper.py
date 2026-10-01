import random

choices = ["rock", "paper", "scissor"]
computer=random.choice(1)
while True:
    print("+**********choose from roak,paper,sicssor")

    choice = int(input("Enter choice :"))
    print(computer)

    if choice==computer:
        print("draw !!")

    elif choice=="roak" and computer=="paper":
        print("You Lose")
            
    elif choice=="paper" and computer=="scissor":
        print("You Lose")
        
    elif choice=="scissor" and computer=="roak":
        print("You Lose")

    elif choice==4:
        print("Exit")
        break

    else:
        print("Choice Is Invalid !!")
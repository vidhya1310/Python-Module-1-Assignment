import random
class bank:
    def ac_registar(self):
        ac_no=random.randint(1001,9999)
        name=input("Enter Name :")
        password=int(input("Enter Password :"))
        mobile=int(input("Enter Mobile :"))
        bal=5000
        ac_no=1234
        print("Your account is open and intial balance :")
        print("Account Number is :",ac_no)
        self.bal=bal


    def deposit(self):
        damount=int(input("Enter Deposit Amount :"))

        self.bal+=damount

        print("Deposit Amount :")
        
    def deposit(self):
        wamount=int(input("Enter Widraw Amount :"))

        self.bal-=wamount

        print("Widraw Amount Sucessfully ! :")

        def check_bal(self):
            print("balance :",self.bal)
obj=bank()

Menu="""
press 1 For Account Register
press 2 for exit
"""
print(Menu)
choice =int(input("Enter Choice :"))

if choice==1:
    obj.ac_registar()

while True:

    Menu="""
    press 1 for deposit
    press 2 for withdraw
    press 1 for check balance
    press 1 for exit
    """

    print(Menu)
    choice1 =int(input("Enter Choice :"))
    if choice1==1:
        if obj.bal>=10000:
            obj.deposit()
        else:
            print("Insufficient Balance")

    elif choice1==2:
        if obj.bal>=1000:
            obj.withdraw()
            obj.check_bal()
        else:                    
            print("Insufficient Balance")                                           

    elif choice1==3:
        obj.check_bal()

    elif choice1==4:
        print("Thank Uh!")
        break
    else:
        print("Invalid Choise!")
        break
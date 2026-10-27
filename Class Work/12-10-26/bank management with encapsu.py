
class bank:

    def ac_registar(self):
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
        if damount>=10000:
            print("Insufficient Balance")
            return
        self.bal+=damount
        print("Deposit Amount Sucessfully ! :")
        
    def deposit(self):
        wamount=int(input("Enter Widraw Amount :"))
        if wamount>=10000:
            print("Insufficient Balance")
            return
        self.bal-=wamount
        print("Widraw Amount Sucessfully ! :")

        def check_bal(self):
            print("Current Balance is :",self.bal)
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
        obj.deposit()

    elif choice1==2:
        obj.withdraw()

    elif choice1==3:
        obj.check_bal()

    elif choice1==4:
        print("Thank Uh!")
        break
    
    else:
        print("Invalid Choise!")
        break

            
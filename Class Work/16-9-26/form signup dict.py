import random
otp = random.randint(1001,9999)

d={}

while True:

    menu='''
    Press 1 for signup
    Press 2 for login
    Press 3 for forgot password
    Press 4 for exit
    '''

    print(menu)
    choice=int(input("Enter Choice :"))

    if choice==1:
        name=input("Enter Name :")
        email=input("Enter Email :")
        mobile=int(input("Enter Mobile :"))
        password=input("Enter Password :")
        cpassword=input("Enter Confrim password :")

        if password == cpassword:
            d['email']=email
            d['mobile']=mobile
            d['password']=password

            print("Signup Sucessssfully !!")

        else:
            print("Password & Confrim Password Does Not Match !!")

    elif choice==2:
        email= input("Enter Email :")
        password = input("Enter Password :")

        if d['email']==email and d['password']==password:
            print("login sucessfully")

        else:
            print("Invalid credentials !!")

    elif choice==3:
        mobile=int(input("Enter mobile :"))

        if d['mobile']==mobile:
            print("*********Your Otp is :",otp)

            uotp = int(input("Enter Otp :"))

            if otp==uotp:
                password=input("Enter Password :")

                d['password']=password
                print("Password Updated !")

            else:
                print("Invalid otp !")

        else:
            print("Mobile number does not exist")

    elif choice==4:
        print("Thank You !")
        break
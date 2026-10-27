from tkinter import *

def login():
    root = Tk()
    root.geometry("500x500")
    root.title("Login Form !")

    name=Label(root,text="Enter Name",font=("calibri",18,"bold"))
    name.place(x=50,y=50)

    email=Label(root,text="Enter Email",font=("calibri",18,"bold"))
    email.place(x=50,y=100)

    mobile=Label(root,text="Enter Mobile",font=("calibri",18,"bold"))
    mobile.place(x=50,y=150)

    password=Label(root,text="Enter Password",font=("calibri",18,"bold"))
    password.place(x=50,y=200)

    cpassword=Label(root,text="Enter Cpassword",font=("calibri",18,"bold"))
    cpassword.place(x=50,y=250)

    ename=Entry(root,bg="pink")
    ename.place(x=280,y=60)

    eemail=Entry(root,bg="pink")
    eemail.place(x=280,y=110)

    emobile=Entry(root,bg="pink")
    emobile.place(x=280,y=160)

    epassword=Entry(root,bg="pink")
    epassword.place(x=280,y=210)

    ecpassword=Entry(root,bg="pink")
    ecpassword.place(x=280,y=260)

    loginbtn = Button(root,bg="lightblue",fg="black",font=("calibri",20,"italic","bold"),text="Login",command=login)
    loginbtn.place(x=50,y=340)

    root.mainloop() 

login()
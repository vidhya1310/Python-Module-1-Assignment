from tkinter import *
from login import login
root = Tk()

root.geometry("500x500")
root.title("Registration Form !")

name=Label(root,fg="black",text="Enter Name",font=("calibri",18,"bold"))
name.place(x=50,y=50)

email=Label(root,fg="black",text="Enter Email",font=("calibri",18,"bold"))
email.place(x=50,y=100)

mobile=Label(root,fg="black",text="Enter Mobile",font=("calibri",18,"bold"))
mobile.place(x=50,y=150)

password=Label(root,fg="black",text="Enter Password",font=("calibri",18,"bold"))
password.place(x=50,y=200)

cpassword=Label(root,fg="black",text="Enter Cpassword",font=("calibri",18,"bold"))
cpassword.place(x=50,y=250)

ename=Entry(root,bg="lightblue")
ename.place(x=280,y=60)

eemail=Entry(root,bg="lightblue")
eemail.place(x=280,y=110)

emobile=Entry(root,bg="lightblue")
emobile.place(x=280,y=160)

epassword=Entry(root,bg="lightblue")
epassword.place(x=280,y=210)

ecpassword=Entry(root,bg="lightblue")
ecpassword.place(x=280,y=260)

insert = Button(root,fg="blue",font=("calibri",18,"italic","bold"),text="Insert",command=login)
insert.place(x=50,y=340)

update = Button(root,fg="red",font=("calibri",18,"italic","bold"),text="Update",)
update.place(x=140,y=340)

delete = Button(root,fg="green",font=("calibri",18,"italic","bold"),text="Delete")
delete.place(x=250,y=340)

search = Button(root,fg="orange",font=("calibri",18,"italic","bold"),text="Search")
search.place(x=350,y=340)

root.mainloop()
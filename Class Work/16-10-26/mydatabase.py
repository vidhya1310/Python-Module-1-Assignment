from database import *

mydb = pymysql.connect(host="localhost",user="root",password="",database="Test1")
mycursor = mydb.cursor()

class database:
    def __init__(self):
        self.mydb = pymysql.connect(host="localhost",user="root",password="")
           
while True:
    menu="""
    press 1 to Insert data
    press 2 to Update data
    press 3 to Delete data
    press 4 to Fatch
    press 5 to Exit
"""
    print(menu)
    chioce=int(input("Enter your choice: "))

    if chioce==1:
        name=input("Enter name: ")
        mobile=int(input("Enter mobile: "))

        query="Insert into Test1 (name,mobile) values ('%s','%s')"
        args=(name,mobile)

        mycursor.execute(query % args)
        mydb.commit()
        print("Data inserted")

    elif chioce==2:
        id=int(input("Enter id: "))
        name=input("Enter name: ")
        mobile=int(input("Enter mobile: "))

        query="UPDATE Test1 SET name='%s',mobile='%s' WHERE id='%s'"
        args=(name,mobile,id)

        mycursor.execute(query % args)
        mydb.commit()
        print("Data updated")

    elif chioce==3:
        id=int(input("Enter id: "))
        query="DELETE FROM Test1 WHERE id='%s'"
        args=(id)

        mycursor.execute(query % args)
        mydb.commit()
        print("Data deleted")

    elif chioce==4:
        query="SELECT * FROM Test1"
        mycursor.execute(query)
        data=mycursor.fetchall()
        print(data)

    elif chioce==5:
        print("Exit")
    else:
        print("Invalid choice")
        
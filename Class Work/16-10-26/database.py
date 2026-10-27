import pymysql

mydb = pymysql.connect(host="localhost",user="root",password="")

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS Test1")
mydb.commit()

mydb = pymysql.connect(host="localhost",user="root",password="",database="Test1")
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS Test1(id int primary key auto_increment,name varchar(60),mobile bigint)")
mydb.commit()
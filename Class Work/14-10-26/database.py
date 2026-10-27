import pymysql

mydb = pymysql.connect(host="localhost",user="root",password="")                        
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS python830")
mydb.commit()

mydb = pymysql.connect(host="localhost",user="root",password="",database="python830")
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS python380(id int primary key auto_increment,name varchar(60),mobile bigint)")
mydb.commit()
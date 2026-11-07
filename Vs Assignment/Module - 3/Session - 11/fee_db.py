
import pymysql

# Connect to MySQL without database
conn = pymysql.connect(
    host="localhost",
    user="root",
    password=""
)

cursor = conn.cursor()

# Create database
cursor.execute(
    "CREATE DATABASE IF NOT EXISTS tuition_fee_db"
)

cursor.close()
conn.close()

# Connect with database
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="tuition_fee_db"
)

cursor = conn.cursor()

# Create students table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        class_name VARCHAR(50),
        monthly_fee DECIMAL(10,2)
    )
""")

conn.commit()

print("Table ready")

cursor.close()
conn.close()

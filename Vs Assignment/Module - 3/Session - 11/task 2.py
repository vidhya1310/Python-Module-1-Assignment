
import pymysql

# Connect to MySQL
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="tuition_fee_db"
)

cursor = conn.cursor()

# Add student function
def add_student(name, class_name, monthly_fee):

    query = """
        INSERT INTO students (name, class_name, monthly_fee)
        VALUES (%s, %s, %s)
    """

    values = (name, class_name, monthly_fee)

    cursor.execute(query, values)
    conn.commit()

    print("Student added successfully!")


# Menu loop
while True:

    print("\n===== TUITION FEE TRACKER =====")
    print("1. Add Student")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        name = input("Enter student name: ")
        class_name = input("Enter class name: ")
        monthly_fee = float(input("Enter monthly fee: "))

        add_student(name, class_name, monthly_fee)

    elif choice == "0":

        print("Thank you!")
        break

    else:
        print("Invalid choice!")

cursor.close()
conn.close()

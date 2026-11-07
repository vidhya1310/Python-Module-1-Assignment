
import pymysql

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="tuition_fee_db"
)

cursor = conn.cursor()


# Add student
def add_student(name, class_name, monthly_fee):

    query = """
        INSERT INTO students (name, class_name, monthly_fee)
        VALUES (%s, %s, %s)
    """

    cursor.execute(query, (name, class_name, monthly_fee))
    conn.commit()

    print("Student added successfully!")


# View all students
def view_students():

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    if students:

        print("\nID   Name       Class       Monthly Fee")
        print("-----------------------------------------")

        for student in students:
            print(
                f"{student[0]:<5}"
                f"{student[1]:<11}"
                f"{student[2]:<12}"
                f"Rs. {student[3]}"
            )

    else:
        print("No students found")


# Search students by class
def search_by_class(class_name):

    query = """
        SELECT * FROM students
        WHERE class_name = %s
    """

    cursor.execute(query, (class_name,))

    students = cursor.fetchall()

    if students:

        print("\nID   Name       Class       Monthly Fee")
        print("-----------------------------------------")

        for student in students:
            print(
                f"{student[0]:<5}"
                f"{student[1]:<11}"
                f"{student[2]:<12}"
                f"Rs. {student[3]}"
            )

    else:
        print("No students found")


# Menu
while True:

    print("\n===== TUITION FEE TRACKER =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search By Class")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        name = input("Enter student name: ")
        class_name = input("Enter class name: ")
        monthly_fee = float(input("Enter monthly fee: "))

        add_student(name, class_name, monthly_fee)

    elif choice == "2":

        view_students()

    elif choice == "3":

        class_name = input("Enter class name: ")
        search_by_class(class_name)

    elif choice == "0":

        print("Thank you!")
        break

    else:
        print("Invalid choice!")

cursor.close()
conn.close()

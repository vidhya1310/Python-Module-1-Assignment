
import pymysql

# Connect to MySQL database
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="tuition_fee_db"
)

cursor = conn.cursor()


# 1. Add student
def add_student(name, class_name, monthly_fee):

    query = """
        INSERT INTO students (name, class_name, monthly_fee)
        VALUES (%s, %s, %s)
    """

    values = (name, class_name, monthly_fee)

    cursor.execute(query, values)
    conn.commit()

    print("Student added successfully!")


# 2. View all students
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


# 3. Search by class
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


# 4. Update student fee
def update_fee(student_id, new_fee):

    query = """
        UPDATE students
        SET monthly_fee = %s
        WHERE id = %s
    """

    cursor.execute(query, (new_fee, student_id))
    conn.commit()

    if cursor.rowcount == 0:
        print("No such student")
    else:
        print("Fee updated successfully!")


# 5. Delete student
def delete_student(student_id):

    query = """
        DELETE FROM students
        WHERE id = %s
    """

    cursor.execute(query, (student_id,))
    conn.commit()

    if cursor.rowcount == 0:
        print("No such student")
    else:
        print("Student deleted successfully!")


# Main menu
while True:

    print("\n===== TUITION FEE TRACKER =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search By Class")
    print("4. Update Fee")
    print("5. Delete Student")
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

    elif choice == "4":

        student_id = int(input("Enter student ID: "))
        new_fee = float(input("Enter new monthly fee: "))

        update_fee(student_id, new_fee)

    elif choice == "5":

        student_id = int(input("Enter student ID: "))

        delete_student(student_id)

    elif choice == "0":

        print("Thank you for using Tuition Fee Tracker!")
        break

    else:
        print("Invalid choice!")


# Close database connection
cursor.close()
conn.close()

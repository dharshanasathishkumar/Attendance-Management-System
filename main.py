from datetime import date
def add_student():
    student_id = input("Enter student ID: ")

    if student_exists(student_id):
        print("Student already exists!")
        return
    
    name = input("Enter student name: ")
    department = input("Enter department: ")

    with open("students.csv", "a") as file:
        file.write(f"\n{student_id},{name},{department}")

    print("Student added successfully!")

def student_exists(student_id):
    with open("students.csv", "r") as file:
        for line in file:
            if line.startswith(student_id + ","):
                return True
    return False


def view_students():
    with open("students.csv", "r") as file:
        print("\n--- Student List ---")
        for line in file:
            print(line.strip())


def mark_attendance():
    student_id = input("Enter student ID: ")
    today = date.today()
    status = input("Enter status (Present/Absent): ")

    with open("attendance.csv", "a") as file:
        file.write(f"\n{student_id},{today},{status}")

    print("Attendance marked successfully!")

def view_attendance():
    with open("attendance.csv", "r") as file:
        print("\n--- Attendance Records ---")
        for line in file:
            print(line.strip())

def main():
    while True:
        print("\n Attendance Management System")
        print("1. Add Student")
        print("2. Mark Attendance")
        print("3. View Attendance")
        print("4. View Students")
        print("5. Exit")

        choice=input("Enter Choice:")
        if choice == "1":
            add_student()
        elif choice == "2":
           mark_attendance()
        elif choice == "3":
            view_attendance()
        elif choice == "4":
            view_students()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice")


if __name__=="__main__":
    main()
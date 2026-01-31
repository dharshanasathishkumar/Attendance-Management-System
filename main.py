from datetime import date
def add_student():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    department = input("Enter department: ")

    with open("students.csv", "a") as file:
        file.write(f"\n{student_id},{name},{department}")

    print("Student added successfully!")

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
        print("4. Exit")

        choice=input("Enter Choice:")
        if choice == "1":
            add_student()
        elif choice == "2":
           mark_attendance()
        elif choice == "3":
            view_attendance()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice")


if __name__=="__main__":
    main()
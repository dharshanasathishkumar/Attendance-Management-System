import os
print("Running from:", os.getcwd())

from datetime import date

# ---------------- STUDENT FUNCTIONS ----------------

def student_exists(student_id):
    with open("students.csv", "r") as file:
        for line in file:
            if line.startswith(student_id + ","):
                return True
    return False


def add_student():
    student_id = input("Enter student ID: ")


    if student_exists(student_id):
        print("Student already exists!")
        return

    name = input("Enter student name: ")
    department = input("Enter department: ")

    if student_id == "" or name == "" or department == "":
        print("All fields are required!")
        return


    with open("students.csv", "a") as file:
        file.write(f"\n{student_id},{name},{department}")

    print("Student added successfully!")


def view_students():
    with open("students.csv", "r") as file:
        print("\n--- Student List ---")
        for line in file:
            print(line.strip())


# ---------------- ATTENDANCE FUNCTIONS ----------------

def mark_attendance():
    student_id = input("Enter student ID: ")

    if not student_exists(student_id):
        print("Student not found!")
        return

    today = date.today()
    with open("attendance.csv", "r") as file:
        for line in file:
            if f"{student_id},{today}" in line:
                print("Attendance already marked for today!")
                return

    status = input("Enter status (Present/Absent): ").strip().capitalize()

    if status not in ["Present", "Absent"]:
        print("Invalid status! Please enter Present or Absent only.")
        return


    with open("attendance.csv", "a") as file:
        file.write(f"{student_id},{today},{status}\n")

    print("Attendance marked successfully!")


def view_attendance():
    with open("attendance.csv", "r") as file:
        print("\n--- Attendance Records ---")
        for line in file:
            print(line.strip())


def view_attendance_by_date():
    search_date = input("Enter date (YYYY-MM-DD): ")
    print("\n--- Attendance on", search_date, "---")
    print("\nID | Date | Status")
    print("-" * 25)


    with open("attendance.csv", "r") as file:
        for line in file:
            if search_date in line:
                print(line.strip())


# ---------------- MAIN MENU ----------------

def main():
    while True:
        print("\nAttendance Management System")
        print("1. Add Student")
        print("2. Mark Attendance")
        print("3. View Attendance")
        print("4. View Students")
        print("5. View Attendance by Date")
        print("6. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            mark_attendance()
        elif choice == "3":
            view_attendance()
        elif choice == "4":
            view_students()
        elif choice == "5":
            view_attendance_by_date()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()

def add_student():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    department = input("Enter department: ")

    with open("students.csv", "a") as file:
        file.write(f"\n{student_id},{name},{department}")

    print("Student added successfully!")

def main():
    while True:
        print("Attendance Management System")
        print("1. Add Student")

        choice=input("Enter Choice:")
        if choice == "1":
            add_student()


if __name__=="__main__":
    main()

from db import get_connection


from flask import Flask, render_template, request, redirect
app = Flask(__name__)



@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add-student", methods=["GET", "POST"])
def add_student_page():
    if request.method == "POST":
        student_id = request.form["student_id"]
        name = request.form["name"]
        department = request.form["department"]

        result = add_student(student_id, name, department)

        return redirect("/")

    return render_template("add_student.html")

@app.route("/students")
def view_students():
    students = get_all_students()
    return render_template("students.html", students=students)

@app.route("/attendance", methods=["GET", "POST"])
def attendance_page():
    if request.method == "POST":
        student_id = request.form["student_id"]
        date = request.form["date"]
        status = request.form["status"]

        mark_attendance(student_id, date, status)
        return redirect("/attendance")

    records = get_attendance()
    return render_template("attendance.html", records=records)





def student_exists(student_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT 1 FROM students WHERE id = %s", (student_id,))
    exists = cursor.fetchone() is not None

    conn.close()
    return exists


def add_student(student_id, name, department):
    if student_exists(student_id):
        return "exists"

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students (id, name, department) VALUES (%s,%s,%s)",
        (student_id, name, department)
    )

    conn.commit()
    conn.close()
    return "added"

def get_all_students():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, department FROM students")
    rows = cursor.fetchall()

    conn.close()

    students = []
    for row in rows:
        students.append({
            "id": row[0],
            "name": row[1],
            "department": row[2]
        })

    return students

def get_attendance():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT student_id, date, status
        FROM attendance
    """)

    rows = cursor.fetchall()
    conn.close()
    return rows

def mark_attendance(student_id, date, status):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO attendance (student_id, date, status) VALUES (?, ?, ?)",
        (student_id, date, status)
    )

    conn.commit()
    conn.close()






if __name__ == "__main__":
    app.run(debug=True)


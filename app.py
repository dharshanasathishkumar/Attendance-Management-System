from db import create_tables
from db import get_connection

create_tables()

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


def student_exists(student_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT 1 FROM students WHERE id = ?", (student_id,))
    exists = cursor.fetchone() is not None

    conn.close()
    return exists


def add_student(student_id, name, department):
    if student_exists(student_id):
        return "exists"

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students (id, name, department) VALUES (?, ?, ?)",
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




if __name__ == "__main__":
    app.run(debug=True)


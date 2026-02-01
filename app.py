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
    with open("students.csv", "r") as file:
        for line in file:
            if line.startswith(student_id + ","):
                return True
    return False

def add_student(student_id, name, department):
    if student_exists(student_id):
        return "exists"

    with open("students.csv", "a") as file:
        file.write(f"{student_id},{name},{department}\n")

    return "added"
def get_all_students():
    students = []
    with open("students.csv", "r") as file:
        for line in file:
            data = line.strip().split(",")
            if len(data) == 3:
                students.append({
                    "id": data[0],
                    "name": data[1],
                    "department": data[2]
                })
    return students



if __name__ == "__main__":
    app.run(debug=True)


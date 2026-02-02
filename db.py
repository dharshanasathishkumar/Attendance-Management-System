import sqlite3

def get_connection():
    conn = sqlite3.connect("attendance.db")
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn



def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        department TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS attendance (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id TEXT,
        date TEXT,
        status TEXT,
        FOREIGN KEY(student_id) REFERENCES students(id)
    )
    """)

    conn.commit()
    conn.close()

def mark_attendance(student_id, date, status):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO attendance (student_id, date, status) VALUES (?, ?, ?)",
        (student_id, date, status)
    )
    conn.commit()
    conn.close()
def get_attendance():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM attendance")
    rows = cursor.fetchall()
    conn.close()
    return rows



if __name__ == "__main__":
    create_tables()

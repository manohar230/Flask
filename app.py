from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)
DB_NAME = 'feedback.db'

# Create the database and table if not exists
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_name TEXT NOT NULL,
            email TEXT NOT NULL,
            comment TEXT NOT NULL,
            submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        comment = request.form['comment']

        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        # ⚠️ Fix: Use ? placeholders instead of %s for SQLite
        cursor.execute("INSERT INTO feedback (student_name, email, comment) VALUES (?, ?, ?)", 
                       (name, email, comment))
        conn.commit()
        conn.close()
        return redirect('/')
    return render_template('feedback.html')

@app.route('/admin')
def admin():
    conn = sqlite3.connect(DB_NAME)
    # ⚠️ Fix: Use Row factory to access columns by name
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM feedback ORDER BY submitted_at DESC")
    feedbacks = cursor.fetchall()
    conn.close()
    return render_template('admin.html', feedbacks=feedbacks)

if __name__ == '__main__':
    init_db()  # Ensure table exists before running
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Ajay@1906",
        database="notes_db"
    )

@app.route('/', methods=['GET', 'POST'])
def index():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    # Always fetch notes for rendering
    cursor.execute("SELECT * FROM notes ORDER BY id DESC")
    notes = cursor.fetchall()

    if request.method == 'POST':
        note = request.form.get('notes', '').strip()

        # VALIDATION GOES HERE
        if not note:
            cursor.close()
            connection.close()
            return render_template(
                'index.html',
                notes=notes,
                error="Note cannot be empty"
            ), 400

        cursor.execute(
            "INSERT INTO notes (content) VALUES (%s)",
            (note,)
        )
        connection.commit()
        cursor.close()
        connection.close()
        return redirect(url_for('index'))

    cursor.close()
    connection.close()
    return render_template('index.html', notes=notes)

# Edit notes by ID
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_note(id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    if request.method == 'POST':
        updated_content = request.form.get('notes')

        if not updated_content:
            cursor.close()
            connection.close()
            return "Note cannot be empty", 400

        cursor.execute(
            "UPDATE notes SET content = %s WHERE id = %s",
            (updated_content, id)
        )
        connection.commit()
        cursor.close()
        connection.close()
        return redirect(url_for('index'))

    cursor.execute("SELECT * FROM notes WHERE id = %s", (id,))
    note = cursor.fetchone()

    cursor.close()
    connection.close()

    if not note:
        return "Note not found", 404

    return render_template('edit.html', note=note)

# Delete by ID

@app.route('/delete/<int:id>', methods=['POST'])
def delete_note(id):
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("DELETE FROM notes WHERE id = %s", (id,))
    connection.commit()

    cursor.close()
    connection.close()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

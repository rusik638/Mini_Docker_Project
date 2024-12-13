from flask import Flask, render_template, request
import psycopg2


app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        dbname="ruslan",
        user="postgres",
        password="",
        host="localhost",
        port="5432"
    )
    return conn

@app.route('/')
def index():
    lvl = request.args.get("lvl")
    conn = get_db_connection()
    cursor = conn.cursor()
    if lvl and lvl.isdigit():
        cursor.execute("SELECT * FROM courses WHERE level = '{}'".format(lvl))
    else:
        cursor.execute("SELECT * FROM courses")
    courses = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', courses=courses, selected_lvl=lvl)

if __name__ == '__main__':
    app.run(debug=True)
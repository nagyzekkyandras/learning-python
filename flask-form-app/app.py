from flask import Flask, render_template, request, session
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
import yaml
import os

app = Flask(__name__)

# confugure DB
db = yaml.safe_load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

app.config['SECRET_KEY'] = os.urandom(24)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        form = request.form
        name = form['name']
        age = form['age']
        cur = mysql.connection.cursor()
        name = generate_password_hash(name)
        cur.execute("INSERT INTO employee(name, age) VALUES(%s, %s)",(name, age))
        mysql.connection.commit()
    return render_template('index.html')

@app.route('/employees')
def employees():
    cur = mysql.connection.cursor()
    result_value = cur.execute("SELECT * FROM employee")
    if result_value > 0:
        employees = cur.fetchall()
        session['username'] = employees[0]['name']
        return(check_password_hash(employees[1]['name'], 'sunday'))
#        return render_template('employees.html', employees=employees)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

from unittest import result
from flask import Flask, redirect, render_template, request
from flask_bootstrap import Bootstrap
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)
Bootstrap(app)

# confugure DB
db = yaml.safe_load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']
mysql = MySQL(app)

@app.route('/')
def index():
    fruits=['Apple', 'Kiwi', 'Banana']
    return render_template('index.html', fruits=fruits)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/extends')
def extends():
    return render_template('extends.html')

@app.route('/css')
def css():
    return render_template('css.html')

# select minta
@app.route('/mysqlselect')
def mysqlselect():
    cur = mysql.connection.cursor()
    cur.execute("""SELECT * FROM user""")
    rv = cur.fetchall()
    return str(rv)

# insert után dobjon a select-es oldalra
@app.route('/mysqlinsert')
def mysqlinsert():
    cur = mysql.connection.cursor()
    cur.execute("""insert into user(username) values('Andris');""")
    mysql.connection.commit()
    return redirect('/mysqlselect')

@app.route('/mysqlselect2')
def mysqlselect2():
    cur = mysql.connection.cursor()
    result_value = cur.execute("SELECT * FROM user")
    if result_value > 0:
        users = cur.fetchall()
        print(users) # log-ba is jelenjen meg
    return str(users)

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        return request.form['password']
    return render_template('form.html')

@app.errorhandler(404)
def page_not_found(e):
    return 'This page was not found!'

if __name__ == '__main__':
    app.run(debug=False, port=5000)
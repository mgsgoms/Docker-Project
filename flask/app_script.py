from flask import Flask, render_template, request
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'backend'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1nd1a'
app.config['MYSQL_DB'] = 'MYUsers'

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
         details = request.form
         firstName = details['fname']
         lastName = details['lname']
         cur = mysql.connection.cursor()
         cur.execute("INSERT INTO MyUsers(firstName, lastName) VALUES(%s,%s)", (firstName, lastName))
         mysql.connection.commit()
         cur.close()
         return 'success'
    return render_template('index.html')


@app.route('/list', methods=['GET', 'POST'])
def listname():
    if request.method == "GET":
         cur = mysql.connection.cursor()
         cur.execute("SELECT * FROM MyUsers")
         data = cur.fetchall()
    return render_template('listname.html', value=data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')

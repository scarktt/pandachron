from flask import Flask, request, make_response, redirect, render_template
from datetime import datetime
from flask_mysqldb import MySQL


app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'pandachrondb'
mysql = MySQL(app)

if __name__ == "__main__":
    app.run(port=3000, debug=True)


todos = ['TODO 1', 'TODO 2', 'TODO 3']


@app.route('/')
def index():
    current_year = datetime.now().year
    return render_template('base.html', current_year=current_year)


@app.route('/add_task')
def add_task():
    context = {
        'current_year': datetime.now().year
    }
    return render_template('index.html', context)

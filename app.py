from flask import Flask, request, make_response, redirect, render_template
from datetime import datetime


app = Flask(__name__)

if __name__ == "__main__":
    app.run(port = 3000, debug = True)


todos = ['TODO 1', 'TODO 2', 'TODO 3']


@app.route('/')
def index():
    return 'index'

@app.route('/add_task')
def add_task():
    context = {
            'current_year': datetime.now().year
    }
    return render_template('index.html', **context)


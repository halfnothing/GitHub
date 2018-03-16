from flask import render_template
from app import app
from app import forms


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'sabakaebaka'}  # выдуманный пользователь
    posts = [  # список выдуманных постов
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'nickname': 'huec'},
            'body': 'mat ebal!'
        }
    ]



@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', 
        title = 'Sign In',
        form = form)


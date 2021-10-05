from flask import render_template
from app import app
from app.form import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user_account = {'username' : "tony", "name" :""}
    return render_template("index.html", user=user_account)

@app.route('/login')
def login():
    login_form = LoginForm()
    return render_template('login.html', form=login_form)

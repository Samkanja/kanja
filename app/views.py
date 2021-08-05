from app import app
from flask import render_template, redirect, flash
from app.forms import RegistrationForm

@app.route('/')
def homepage():
    return render_template('home.html')

@app.route('/register',methods=['GET', 'POST'])
def login():
    form = RegistrationForm()
    return render_template('register.html', form=form)


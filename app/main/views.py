from flask import render_template,request,redirect, url_for, flash
# from app import app
from . import main
from ..import db, bcrypt
from ..models import Pitch, User
from .forms import Your_pitchForm, RegistrationForm, LoginForm
from flask_login import login_user, current_user, logout_user


#dammy data
# Pitch = pitch.Pitch
pitches = [
    {
    'author': "COret SChafer",
    'your_pitch': "first pitch ever",
    'date_posted': 'April 20, 2019'
    },
    {
    'author': "COret SChafer",
    'your_pitch': "first pitch ever",
    'date_posted': 'April 20, 2019'
    }
]


@main.route('/')
@main.route('/home')
def home():
    return render_template('home.html', pitches=pitches)

@main.route('/about')
def about():
    return "<h1>About Page<h1>"

@main.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data, email =form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}! You can login Now','success')
        return redirect(url_for('main.login'))

    return render_template('register.html', tittle = 'Register', form =form)

@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('main.home'))

        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
            
    return render_template('login.html', tittle = 'Login', form =form)

@main.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.login'))
    




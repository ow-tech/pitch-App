from flask import render_template,request,redirect, url_for, flash
# from app import app
from . import main
from ..models import pitch
from .forms import Your_pitchForm, RegistrationForm, LoginForm


#dammy data
Pitch = pitch.Pitch
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
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))

    return render_template('register.html', tittle = 'Register', form =form)

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == 'wagwanwekon' and form.password.data =='123':
            flash('You have been logged in', 'success')
            return redirect(url_for('home'))

        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
            
    return render_template('login.html', tittle = 'Login', form =form)

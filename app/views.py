from flask import render_template,request,redirect,url_for
from app import app
from .models import pitch
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


#views
# @app.route('/', methods =['GET','POST'])
# def index():
#     '''
#     View root page function that returns the idnex page and its ata

#     '''

#     form = Your_pitchForm()

#     if form.validate_on_submit():
#         new_pitch = request.form
#         return render_template("new_pitch.html", new_pitch = new_pitch)
#         form = Your_pitchForm()
#         pitch = new_pitch

#     return render_template('index.html', form = form)

# @app.route('/pitches')
# def pitches():
#     return render_template('pitches.html')



    # return render_template('index.html')

# app.route('pitch/', methods =['GET','POST'])
# def new_pitch():

#     form = Your_pitchForm()

#     if form.validate_on_submit():
#         category = form.category.data
#         Your_pitch = form.Your_pitch.data
#         new_pitch = Pitch(your_pitch)
#         new_pitch.save_pitch()
#         return redirect(url_for('index'))

#     return render_template('new_pitch.html', form = pitch_form)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', pitches=pitches)

@app.route('/about')
def about():
    return "<h1>About Page<h1>"

@app.route('/register')
def register():
    form = RegistrationForm()

    return render_template('register.html', tittle = 'Register', form =form)

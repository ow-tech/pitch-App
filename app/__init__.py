from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap




#Initializing application

app = Flask(__name__, instance_relative_config = True)
# app.config['SECRET_KEY'] ='eead0cf8e905a3ea9e505fb0ace2a3d2'

#setting up configuration

app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

# Initializing Flask Extensions
bootstrap = Bootstrap(app)

from app import views


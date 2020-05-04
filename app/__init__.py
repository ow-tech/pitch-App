from flask import Flask
# from .config import DevConfig
# from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'login'
#Initializing application
def create_app(config_name):

    app = Flask(__name__)
    # app.config['SECRET_KEY'] ='eead0cf8e905a3ea9e505fb0ace2a3d2'
    # Creating the app configurations
    app.config.from_object(config_options[config_name])
    # app.config.from_pyfile('config.py')

    # Initializing Flask Extensions
    # bootsrap.init_app(app)
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)


    #Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # from .auth import auth as auth_blueprint
    # app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')



    return app

    # from app import views


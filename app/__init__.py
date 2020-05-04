from flask import Flask
# from .config import DevConfig
# from flask_bootstrap import Bootstrap
from config import config_options




#Initializing application
def create_app(config_name):

    app = Flask(__name__)
    # app.config['SECRET_KEY'] ='eead0cf8e905a3ea9e505fb0ace2a3d2'
    # Creating the app configurations
    app.config.from_object(config_options[config_name])
    # app.config.from_pyfile('config.py')

    # Initializing Flask Extensions
    # bootsrap.init_app(app)
    # db.init_app(app)


    #Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

    # from app import views


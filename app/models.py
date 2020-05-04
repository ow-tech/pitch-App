from . import db
from datetime import datetime



    # """
    # Pitch class to define Pitch objects
    # """
    # all_pitches = []

    # def __init__ (self,author, your_pitch, date_posted):
    #     self.your_pitch = your_pitch
    #     self.author = author
    #     self.date_posted = date_posted

    # def save_pitch(self):
    #     Pitch.all_pitches.append(self)


    # @classmethod
    # def clear_pitches(cls):
    #     Pitch.all_pitches.clear()

class User (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), unique = True, nullable = False)
    email = db.Column(db.String(150), unique = True, nullable = False)
    image_file = db.Column(db.String(20), nullable = False, default ='mypic.jpg')
    password = db.Column(db.String(60), nullable = False)
    pitches = db.relationship('Pitch', backref='author', lazy= True)


    def __repr__(self):
        return f'User ("{self.username}","{self.email}","{self.image_file}")'

class Pitch (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    # author = db.Column(db.String(50), nullable = False)
    date_posted = db.Column(db.DateTime, nullable = False, default= datetime.utcnow)
    your_pitch = db.Column(db.Text, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)


    def __repr__(self):
        return f'Pitch ("{self.your_pitch}","{self.date_posted}")'
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    '''
    name = db.Column(db.String(150))
    species = db.Column(db.String(150)) # cat or dog
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # refers to pet's owner
    date_added = db.Column(db.DateTime(timezone=True), default=func.now())
    date_of_birth = db.Column(db.DateTime(timezone=True))
    breed = db.Column(db.String(150)) 
    color_pattern = db.Column(db.String(150)) 
    location = db.Column(db.String(150)) # city, state
    '''

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    # last_name = db.Column(db.String(150))
    pets = db.relationship('Pet')
    # date_added = db.Column(db.DateTime(timezone=True), default=func.now())

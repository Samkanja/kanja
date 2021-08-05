from enum import unique
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120),unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable = False, default='default.jpg')
    password = db.Column(db.String(60), nullable= False)
    
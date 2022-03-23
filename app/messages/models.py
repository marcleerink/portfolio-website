from app.extensions.database import db
from datetime import datetime

class Date(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120))
    
    messages = db.relationship('Message', backref='user', lazy=True)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(120))
    message = db.Column(db.Text())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
     
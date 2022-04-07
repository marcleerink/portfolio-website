from app.extensions.database import db, CrudMixin
from flask_login import UserMixin
from datetime import datetime

class User(UserMixin, db.Model, CrudMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120))
    
    messages_sent = db.relationship('Message', backref='user')

class Message(db.Model, CrudMixin):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(120))
    message = db.Column(db.String(5000))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    timestamp = db.Column(db.DateTime, default = datetime.today().replace(microsecond=0))

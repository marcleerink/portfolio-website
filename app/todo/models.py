from app.extensions.database import db, CrudMixin

class Todo(db.Model, CrudMixin):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(80), unique=True)
    page = db.Column(db.String(80))
    priority = db.Column(db.Integer())
from app.extensions.database import db, CrudMixin
class Projects(db.Model, CrudMixin):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(80), unique=True)
    title = db.Column(db.String(80))
    content = db.Column(db.String(10000))
    link = db.Column(db.String(260))
    code_link = db.Column(db.String(260))
    priority = db.Column(db.Integer())
    image_url = db.Column(db.String(260))
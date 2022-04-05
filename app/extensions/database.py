from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
class CrudMixin():

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return 
        
db = SQLAlchemy()
migrate = Migrate()
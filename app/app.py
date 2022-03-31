from flask import Flask
from . import todo, simple_pages, messages
from app.extensions.database import db, migrate
from flask_login import LoginManager


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')
    app.secret_key = 'JGKS$A%)GSH(%$JANG$)%MSN%(SHS'

    login_manager = LoginManager()
    login_manager.login_view = 'messages.get_login'
    login_manager.init_app(app)
    
    from app.messages.models import User

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    register_extensions(app)
    register_blueprints(app)

    return app
 
#Blueprints
def register_blueprints(app: Flask):
    app.register_blueprint(simple_pages.routes.blueprint)
    app.register_blueprint(todo.routes.blueprint)
    app.register_blueprint(messages.routes.blueprint)

def register_extensions(app: Flask):
    db.init_app(app)
    migrate.init_app(app, db)
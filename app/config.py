from dotenv import load_dotenv
from os import environ

load_dotenv()
SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = False
TODO_PER_PAGE = 2

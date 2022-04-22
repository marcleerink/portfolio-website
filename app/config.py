from os import environ
from dotenv import load_dotenv

load_dotenv()

SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL').replace('postgres://', 'postgresql://', 1)
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = False
TODO_PER_PAGE = 2
PROJECTS_PER_PAGE = 3
API_KEY = environ.get('API_KEY')
PLANET_API_KEY = environ.get('PLANET_API_KEY')
SECRET_KEY = environ.get('SECRET_KEY')
MY_EMAIL_PW = environ.get('MY_EMAIL_PW')
MY_EMAIL = environ.get('MY_EMAIL')
MAIL_SERVER='smtp.googlemail.com'
MAIL_PORT=587
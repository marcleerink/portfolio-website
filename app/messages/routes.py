from pyexpat.errors import messages
from flask import Blueprint, render_template, request, url_for, redirect, flash, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from .models import Message, User
from flask_login import LoginManager, login_required, login_user, current_user, logout_user

blueprint = Blueprint('messages', __name__)


@blueprint.get('/sign-up')
def get_signup():
    return render_template('messages/signup.html')

@blueprint.post('/sign-up')
def post_signup():
    #create a user
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')

    if password !=confirm_password:
        flash('Passwords not identical, try again')
        return redirect(url_for('messages.get_signup'))

    user = User.query.filter_by(email=email).first()

    if user:
        flash('Email already exists. Do you have an account already?')
        return redirect(url_for('messages.get_signup'))

    new_user = User(name=name, email=email, password=generate_password_hash(password, method='sha256'))
    new_user.save()

    return render_template('messages/login.html')


@blueprint.get('/log-in')
def get_login():
    return render_template('messages/login.html')

@blueprint.post('/log-in')
def post_login():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()
    #check if user exists
    #compare passwords with database
    if not user or not check_password_hash(user.password, password):
        flash ('Incorrect email or password, try again, ')
        return redirect(url_for('messages.get_login'))
    login_user(user, remember=remember)
    return redirect(url_for('messages.profile'))

@blueprint.route('/log-out')
@login_required
def logout():
    logout_user()
    return redirect(url_for('simple_pages.index'))

@blueprint.route('/profile')
def profile():
    messages = Message.query.all()
    return render_template('messages/profile.html', name=current_user.name, email=current_user.email, messages = messages)


@blueprint.get('/contact')
@login_required
def get_contact():
    return render_template('messages/contact_form.html', name=current_user.name, email=current_user.email)

@blueprint.post('/contact')
def post_contact():
    # Create a message
    # message = Message()
    # message.save()

    # messages = Message.query.all()
    subject = request.form.get('subject')
    message = request.form.get('message')

    new_message = Message(subject=subject, message=message)
    new_message.save()
    
    flash('Message sent!')
    return render_template('messages/contact_form.html')
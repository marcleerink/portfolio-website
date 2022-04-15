# from email import message
# from pyexpat.errors import messages
import email
from flask import Blueprint, render_template, request, url_for, redirect, flash, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from .models import Message, User
from flask_login import LoginManager, login_required, login_user, current_user, logout_user
import smtplib
from app.config import MAIL_PORT, MAIL_SERVER, MY_EMAIL, MY_EMAIL_PW


blueprint = Blueprint('messages', __name__)

@blueprint.get('/sign-up')
def get_signup():
    return render_template('messages/signup.html')

@blueprint.post('/sign-up')
def post_signup():
    # get input from form
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')

    # validate input lenght for database record/security 
    if len(name) > 119:
        flash('Name input too long')
        return redirect(url_for('messages.get_signup'))
    elif len(password) > 119:
        flash('Password input too long')
        return redirect(url_for('messages.get_signup'))
    elif len(password) < 8:
        flash('Password must be 8 or more characters')
        return redirect(url_for('messages.get_signup'))

    # validate password
    if password !=confirm_password:
        flash('Passwords not identical, try again')
        return redirect(url_for('messages.get_signup'))
    
    # validate if user already exists
    user = User.query.filter_by(email=email).first()
    if user:
        flash('Email already exists. Do you have an account already?')
        return redirect(url_for('messages.get_signup'))
    else:
        # create user
        new_user = User(name=name, email=email, password=generate_password_hash(password, method='sha256'))
        new_user.save()
        return redirect(url_for('messages.get_login'))


@blueprint.get('/log-in')
def get_login():
    return render_template('messages/login.html')

@blueprint.post('/log-in')
def post_login():
    # get input from form
    email = request.form.get('email')
    password = request.form.get('password')
    
    #check if user exists
    #compare passwords with database
    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        flash ('Incorrect email or password, try again, ')
        return redirect(url_for('messages.get_login'))
    login_user(user)
    return redirect(url_for('messages.profile'))

@blueprint.route('/log-out')
@login_required
def logout():
    logout_user()
    return redirect(url_for('simple_pages.index'))

@blueprint.route('/profile')
@login_required
def profile():
    messages = Message.query.filter_by(user_id= current_user.id).all()
    # messages = current_user.messages_sent.order_by(Message.timestamp.desc())
    
    return render_template('messages/profile.html', name = current_user.name, email = current_user.email, messages = messages)


@blueprint.get('/contact')
@login_required
def get_contact():
    return render_template('messages/contact_form.html', name=current_user.name, email=current_user.email)

@blueprint.post('/contact')
def post_contact():
    # get input from form
    subject = request.form.get('subject')
    message = request.form.get('message')
    user_id = current_user.id

    #check if input isn't to long
    if len(subject) > 119 or len(message) > 4999:
        flash ('Input to long')
    else:
        # Store message in database
        new_message = Message(subject=subject, message=message, user_id = user_id)
        new_message.save()

        # Send message to my email
        try: 
            server = smtplib.SMTP(MAIL_SERVER, MAIL_PORT)
            server.starttls()
            server.login(MY_EMAIL, MY_EMAIL_PW)
            server.sendmail(MY_EMAIL, MY_EMAIL, current_user.email + subject + message)
            flash('Message sent!')
        except smtplib.SMTPException:
            flash('Unable to send mail')
            
    return render_template('messages/contact_form.html', name = current_user.name, email = current_user.email)
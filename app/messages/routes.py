from flask import Blueprint, render_template, request, url_for, redirect
from .models import Message, User
blueprint = Blueprint('messages', __name__)

@blueprint.get('/contact')
def get_contact():

    return render_template('messages/contact_form.html')

@blueprint.post('/contact')
def post_contact():
    # Create a message
    message = Message()
    message.save()

    messages = Message.query.all()
    return render_template('messages/contact_form.html', messages = messages)

@blueprint.get('/login')
def post_login():
    #Create a User
    user = User()
    user.save()

    users = user.query.all()
    return render_template('simple_pages/index.html', users = users)

@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['email'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('simple_pages.index'))
    return render_template('messages/login.html', error=error)

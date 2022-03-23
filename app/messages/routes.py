from flask import Blueprint, render_template
from app.todo.models import Todo

blueprint = Blueprint('messages', __name__)

@blueprint.get('/contact')
def get_contact():
    todo = Todo.query.all()

    return render_template('messages/contact_form.html')

@blueprint.post('/contact')
def post_contact():
    todo = Todo.query.all()
    
    return render_template('messages/contact_form.html')
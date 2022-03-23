from flask import Blueprint, render_template, request, current_app
from app import todo
from .models import Todo

blueprint = Blueprint('todo', __name__)
 
@blueprint.route('/to-do/<slug>')
def pages(slug):
    todo = Todo.query.filter_by(slug=slug).first_or_404()
    return render_template('todo/show.html', todo=todo)

@blueprint.route('/to-do')
def todo():
    page_number = request.args.get('page', 1, type=int)
    todo_pagination = Todo.query.paginate(page_number, current_app.config['TODO_PER_PAGE'])
    return render_template('todo/index.html', todo_pagination = todo_pagination)
from app.app import create_app
from app.todo.models import Todo
from app.extensions.database import db

app = create_app()
app.app_context().push()

to_do_list = {
    'sign-up': {'page' : 'Sign Up', 'priority' : 1},
    'log-in': {'page' : 'Log In', 'priority' : 1},
    'contact': {'page' : 'Contact Form', 'priority' : 2},
    'projects': {'page' : 'Projects', 'priority' : 3},
}

for slug, todo in to_do_list.items():
    new_todo = Todo(slug=slug, page=todo['page'], priority=todo['priority'])
    db.session.add(new_todo)
    
db.session.commit()
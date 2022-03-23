from app.extensions.database import db
from app.todo.models import Todo

def test_todo_update (client):
    # updates todo's properties
    todo = Todo(slug='sign-up', page = 'Sign Up', priority = 1)
    db.session.add(todo)
    db.session.commit()

    todo.page = 'Log In'
    todo.save()

    updated_todo = Todo.query.filter_by(slug='sign-up').first()
    assert updated_todo.name == 'Log In'

def test_todo_delete(client):
    # deletes todo
    todo = Todo(slug='sign-up', page='Sign Up', priority = 1)
    db.session.add(todo)
    db.session.commit()

    todo.delete()

    deleted_todo = Todo.query.filter_by(slug='sign-up').first()
    assert deleted_todo is None

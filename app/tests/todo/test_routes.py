from app.todo.models import Todo

def test_toto_renders_todo(client):
    # Page loads and renders todo
    new_todo = Todo(slug='sign-up', page='Sign Up', priority = 1)
    new_todo.save()

    response = client.get('/to-do')

    assert b'Sign Up' in response.data
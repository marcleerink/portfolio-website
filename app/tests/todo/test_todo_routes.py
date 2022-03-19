def test_todo_content(client):
    # Returns header
    response = client.get('/to-do')
    assert b'<h2> Pages to do</h2>' in response.data
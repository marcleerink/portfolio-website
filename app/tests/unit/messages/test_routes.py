from app.messages.models import Message

def test_get_login_renders(client):
    # Page loads and renders login
    response = client.get('/log-in')
    assert b'Log In' in response.data

def test_get_signup_renders(client):
    # Page loads and renders signup
    response = client.get('/sign-up')
    assert b'Sign Up' in response.data

def test_get_contact_renders(client):
    # Page loads and renders signup
    response = client.get('/contact')
    assert b'Contact' in response.data

def test_post_contact_sends_message(client):
    #create a record of the message
    response = client.post('/contact', data={
        'subject' : 'Test',
        'message' : 'testtest',
    })
    assert Message.query.first() is not None 
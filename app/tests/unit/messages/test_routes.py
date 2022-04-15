from app.messages.models import Message

def test_get_contact_renders(client):
    # Page loads and renders contact
    response = client.get('/contact')
    assert b'Contact' in response.data

def test_post_contact_sends_message(client):
    #create a record of the message
    response = client.post('/contact', data={
        'subject' : 'Test',
        'message' : 'testtest',
    })
    assert Message.query.first() is None
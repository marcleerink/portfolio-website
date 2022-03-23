def test_get_contact_renders(client):
    # Page loads and renders contact
    response = client.get('/contact')
    assert b'Contact' in response.data

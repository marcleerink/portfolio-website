
# Index Page
def test_index_success(client):
    # Page loads
    response = client.get('/')
    assert response.status_code == 200

def test_index_content(client):
    # Returns button html
    response = client.get('/')
    assert b'<i class="fa-solid fa-code"></i>' in response.data



# Sound Artist Page
def test_sound_artist_success(client):
    # Page loads
    response = client.get('/sound-artist')
    assert response.status_code == 200


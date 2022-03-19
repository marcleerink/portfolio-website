
# Index Page
def test_index_success(client):
    # Page loads
    response = client.get('/')
    assert response.status_code == 200

def test_index_content(client):
    # Returns button html
    response = client.get('/')
    assert b'<i class="fa-solid fa-code"></i>' in response.data


#Software Engineer Page
def test_software_engineer_success(client):
    # Page loads
    response = client.get('/software-engineer')
    assert response.status_code == 200

# Sound Artist Page
def test_sound_artist_success(client):
    # Page loads
    response = client.get('/sound-artist')
    assert response.status_code == 200

# Contact Page
def test_contact_success(client):
    # Page loads
    response = client.get('/contact')
    assert response.status_code == 200

#Projects Page
def test_projects_success(client):
    # Page loads
    response = client.get('/projects')
    assert response.status_code == 200

#CV Download
def test_cv_success(client):
    # Page loads
    response = client.get('/cv')
    assert response.status_code == 200


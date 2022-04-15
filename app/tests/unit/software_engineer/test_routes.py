#Software Engineer Page Loads
def test_software_engineer_success(client):
    response = client.get('/software-engineer')
    assert response.status_code == 200

    #Projects Page Loads
def test_projects_success(client):
    response = client.get('/projects')
    assert response.status_code == 200

    #CV Download loads
def test_cv_success(client):
    response = client.get('/cv')
    assert response.status_code == 200
""" INDEX TESTS"""

def test_index_success(client): 
    # Index loads 
    response = client.get('/')
    assert response.status_code == 200


def test_about_success(client): 
    # About loads
    response = client.get('/about')
    assert response.status_code == 200

def test_portrait_success(client): 
    # Street loads
    response = client.get('/portrait')
    assert response.status_code == 200

def test_street_success(client): 
    # Portrait loads
    response = client.get('/street')
    assert response.status_code == 200


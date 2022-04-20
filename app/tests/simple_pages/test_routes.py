from app.models.orders import Order

""" INDEX TESTS"""

# test 1
def test_index_success(client): 
    # Index loads 
    response = client.get('/')
    assert response.status_code == 200

# test 2

def test_about_success(client): 
    # About loads
    response = client.get('/about')
    assert response.status_code == 200

# test 3

def test_portrait_success(client): 
    # Street loads
    response = client.get('/portrait')
    assert response.status_code == 200

# test 4

def test_street_success(client): 
    # Portrait loads
    response = client.get('/street')
    assert response.status_code == 200

# test 5

def test_ind_street_success(client): 
    # Ind loads 
    response = client.get('/street/<name>')
    assert response.status_code == 200

# test 6

def test_ind_portrait_success(client): 
    # Ind loads 
    response = client.get('/portrait/<name>')
    assert response.status_code == 200
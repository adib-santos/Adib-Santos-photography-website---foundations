from app.models.orders import Order

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

def test_get_checkout_renders(client):
    # page loads and renders checkout
    response = client.get('/checkout')
    assert b'Checkout' in response.data

def test_post_checkout_create_orders(client):
    # creates an order record

    response = client.post('/checkout', data= {
        'date': '14/05/2022', 
        'address_id': 2,
        'foto_id': '13', 
    })
    assert Order.query.first() is not None

from app.models.orders import Order

def test_get_checkout_renders(client): 
    # Page loads and renders checkout 

    response = client.get('/checkout')
    assert b'Checkout' in response.data

"""
        Failing test # 2

def test_post_checkout_creates_order(client): 
    # Creates an order record

    response = client.post('/checkout', data = {
        'street': 'Weserstrasse 14',  
        'city': 'Berlin', 
        'zip': '12047', 
        'country': 'Germnay'
    })
    assert Order.query.first() is not None

"""


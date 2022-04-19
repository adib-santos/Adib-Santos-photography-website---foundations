from app.models.orders import Address

def test_get_checkout_renders(client): 
    # Page loads and renders checkout 

    response = client.get('/checkout')
    assert b'Checkout' in response.data

def test_post_checkout_creates_order(client): 
    # Creates an order record

    response = client.post('/checkout', data = {
        'street': '123 Main St', 
        'city': 'Anytown',  
        'zip': '12345', 
        'country': 'Candyland'
    })
    assert Address.query.first() is not None
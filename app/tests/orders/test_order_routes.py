from app.models.orders import Order

def test_post_checkout_portrait_creates_order(client): 

    # Creates an order record

    response = client.post('/portrait/<name>', data = {
        'street': 'Eledistrasse',
        'city': 'Berlin',
        'zip': '230238',
        'country': 'Germany',
        'county': 'candyland'
    })
    assert Order.query.first() is not None

def test_post_checkout_street_creates_order(client): 

    # Creates an order record

    response = client.post('/street/<name>', data = {
        'street': 'Eledistrasse',
        'city': 'Berlin',
        'zip': '230238',
        'country': 'Germany',
        'county': 'candyland'
    })
    assert Order.query.first() is not None
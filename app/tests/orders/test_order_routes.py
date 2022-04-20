from app.models.orders import Order


# test 7.1
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

# test 7.2
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
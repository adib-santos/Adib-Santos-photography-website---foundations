""" INDEX TESTS"""

def test_index_success(client): 
    # Index loads 
    response = client.get('/')
    assert response.status_code == 200

""" SHOP TESTS"""

def test_index_content(client): 
    # Returns welcome text
    response = client.get('/shop')
    assert b'Prints shop' in response.data

def test_shop_success(client): 
    # Shop loads properly
    response = client.get('/shop')
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

""" TXT TESTS """
def test_receipt_download(client): 
    # Returns receipt
    response = client.get('/receipt.txt')
    assert response.headers['Content-Disposition'] == 'attachment; filename=receipt.txt'

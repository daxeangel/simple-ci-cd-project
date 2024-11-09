from app import app

def test_hello_world():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert response.data == b'Hello, World!'

def test_greet():
    response = app.test_client().get('/greet/TestUser')
    assert response.status_code == 200
    assert response.data == b'Hello, TestUser!'

def test_invalid_route():
    response = app.test_client().get('/invalid')
    assert response.status_code == 404
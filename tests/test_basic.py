from flask import url_for
from app.models import User, Post

def test_register(client):
    response = client.post('/register', data={
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'password'
    })
    assert response.status_code == 302  # Redirect to login page
    assert User.query.filter_by(email='test@example.com').first() is not None

def test_login(client):
    client.post('/register', data={
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'password'
    })
    response = client.post('/login', data={
        'email': 'test@example.com',
        'password': 'password'
    })
    assert response.status_code == 302  # Redirect to home page

def test_invalid_login(client):
    response = client.post('/login', data={
        'email': 'wrong@example.com',
        'password': 'wrongpassword'
    })
    assert b'Invalid email or password.' in response.data

def test_create_post(client):
    client.post('/register', data={
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'password'
    })
    client.post('/login', data={
        'email': 'test@example.com',
        'password': 'password'
    })
    response = client.post('/post/new', data={
        'title': 'Test Post',
        'body': 'This is a test post.'
    })
    assert response.status_code == 302  # Redirect to home page
    assert Post.query.filter_by(title='Test Post').first() is not None

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to My Blog' in response.data
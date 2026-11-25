import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.mark.django_db
def test_login_success(client):
    User.objects.create_user(username='login_user', password='StrongP@ssw0rd123')
    
    url = reverse('accounts:login')
    data = {
        'username': 'login_user',
        'password': 'StrongP@ssw0rd123',
    }
    
    response = client.post(url, data)
    
    assert response.status_code == 302
    assert response.wsgi_request.user.is_authenticated


@pytest.mark.django_db
def test_login_fail(client):
    User.objects.create_user(username='login_user', password='StrongP@ssw0rd123')
    
    url = reverse('accounts:login')
    data = {
        'username': 'login_user',
        'password': 'wrong_password',
    }
    
    response = client.post(url, data)
    
    assert response.status_code == 200
    assert not response.wsgi_request.user.is_authenticated
import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.mark.django_db
def test_register(client):
    url = reverse("accounts:register")
    data = {
        "username": "test_user_man",
        "password1": "StrongP@ssw0rd123",
        "password2": "StrongP@ssw0rd123",
        "name": "тест0",
        "surname": "тест0",
        "patronymic": "тест0",
        "birth_date": "2000-01-01",
        "phone": "1234",
        "email": "test0@mail.com",
    }

    response = client.post(url, data)

    assert response.status_code == 302
    assert User.objects.filter(username="test_user_man").exists()

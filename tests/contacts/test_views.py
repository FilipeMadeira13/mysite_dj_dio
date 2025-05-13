from http import HTTPStatus

import pytest

from django.urls import reverse
from django.contrib.auth.models import User, Permission


def test_contact_thanks(client):
    # Given
    name = "John Doe"

    # When
    response = client.get(reverse("contacts:thanks", args=(name,)))

    # Then
    assert response.status_code == HTTPStatus.OK
    assert response.content.decode() == f"Obrigado {name}!"


def test_contact_create_with_unautenticated_user(client):
    # Given
    url = f"{reverse('accounts:login')}?next={reverse('contacts:create')}"

    # When
    response = client.get(reverse("contacts:create"))

    # Then
    assert response.status_code == HTTPStatus.FOUND
    assert response.url == url


@pytest.mark.django_db
def test_contact_create_success(client, django_user_model):
    # Given
    data = {
        "subject": "Test Subject",
        "message": "Test Message",
        "sender": "sender@testemail.com",
        "cc_myself": True,
    }
    user = django_user_model.objects.create_user(
        username="John", email="john@testmail.com", password="123mudar"
    )
    permission = Permission.objects.get(codename="add_contact")
    user.user_permissions.add(permission)

    # When
    client.force_login(user)
    response = client.post(reverse("contacts:create"), data=data)

    # Then
    assert response.status_code == HTTPStatus.FOUND
    assert response.url == reverse("contacts:thanks", args=(data["subject"],))

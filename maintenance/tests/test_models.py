import pytest
from django.test import Client
from .factories import CarFactory


@pytest.mark.django_db
def test_Car_str():
    car = CarFactory()
    assert str(car) == f'{car.make} {car.model}'


@pytest.mark.django_db
def test_car_get_absolute_url():
    car = CarFactory()
    client = Client()
    car.owner.set_password('aaaa')
    car.owner.save()
    logged = client.login(username=car.owner.username,
                          password='aaaa')
    response = client.get(car.get_absolute_url())
    assert logged
    assert response.status_code == 200
    assert response.template_name == ['maintenance/car_detail.html']

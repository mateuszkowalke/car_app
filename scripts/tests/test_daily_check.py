import pytest
from scripts.daily_check import run
from datetime import date, timedelta
from django.core import mail
from maintenance.tests.factories import CarFactory


@pytest.mark.parametrize('execution_number', range(20))
@pytest.mark.django_db
def test_car_no_sending(execution_number):
    car = CarFactory(last_inspection=date.today(),
                     last_insurance=date.today())
    car.owner.set_password('aaaa')
    car.owner.save()
    run([car])
    assert mail.outbox == []


@pytest.mark.django_db
def test_car_insurance_short():
    car = CarFactory(last_inspection=date.today(),
                     last_insurance=date.today()-timedelta(days=360))
    car.owner.set_password('aaaa')
    car.owner.save()
    run([car])
    assert len(mail.outbox) == 1
    assert 'ubezpieczenie' in mail.outbox[0].body


@pytest.mark.django_db
def test_car_inspection_short():
    car = CarFactory(last_inspection=date.today()-timedelta(days=360),
                     last_insurance=date.today())
    car.owner.set_password('aaaa')
    car.owner.save()
    run([car])
    assert len(mail.outbox) == 1
    assert 'przegląd' in mail.outbox[0].body


@pytest.mark.django_db
def test_car_inspection_and_insurance_short():
    car = CarFactory(last_inspection=date.today()-timedelta(days=360),
                     last_insurance=date.today()-timedelta(days=360))
    car.owner.set_password('aaaa')
    car.owner.save()
    run([car])
    assert len(mail.outbox) == 1
    assert 'przegląd i ubezpieczenie' in mail.outbox[0].body

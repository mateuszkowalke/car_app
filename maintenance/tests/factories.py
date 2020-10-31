import factory
from datetime import datetime
from faker import Faker
from maintenance.models import Car
from users.tests.factories import UserFactory


fake = Faker()


class CarFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Car

    make = fake.text(max_nb_chars=64)
    model = fake.text(max_nb_chars=64)
    year = fake.date()
    mileage = fake.random_int()
    oil_service_interval = fake.random_int()
    oil_service_date_last_done = fake.date()
    oil_service_mileage_last_done = fake.random_int()
    oil_service_oil_type = fake.text(max_nb_chars=128)
    last_inspection = fake.date()
    last_insurance = fake.date()
    insurance_duration = fake.random_element(elements=('12', '6', '3', '1'))
    owner = factory.SubFactory(UserFactory)

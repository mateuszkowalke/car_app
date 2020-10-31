import factory
from datetime import datetime
from faker import Faker
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User


fake = Faker()


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User

    username = fake.user_name()
    email = fake.ascii_email()
    password = make_password(fake.password())

from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User


class Car(models.Model):

    INSURANCE_DURATION_CHOICES = [
        ('12', 'rok'),
        ('6', 'pół roku'),
        ('3', 'trzy miesiące'),
        ('1', 'miesiąc'),
    ]

    make = models.CharField(max_length=64, verbose_name='Marka')
    model = models.CharField(max_length=64, verbose_name='Model')
    year = models.DateField(verbose_name='Rok produkcji')
    mileage = models.PositiveIntegerField(verbose_name='Przebieg')
    oil_service_interval = models.PositiveSmallIntegerField(
        verbose_name='Interwał wymiany oleju')
    oil_service_date_last_done = models.DateField(
        verbose_name='Data ostatniej wymiany oleju')
    oil_service_mileage_last_done = models.PositiveIntegerField(
        verbose_name='Przebieg przy ostatniej wymianie oleju')
    oil_service_oil_type = models.CharField(
        max_length=128, verbose_name='Rodzaj oleju')
    last_inspection = models.DateField(
        verbose_name='Data ostatniego przeglądu')
    last_insurance = models.DateField(
        verbose_name='Data zawarcia ostatniej umowy OC')
    insurance_duration = models.CharField(
        max_length=2, choices=INSURANCE_DURATION_CHOICES, verbose_name='Czas trwania umowy OC')
    owner = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name='Właściciel')

    def get_fields_for_detail_template(self):
        """ Gets iterable for the loop in template """
        return [
            (field.verbose_name, self.get_insurance_duration_display() if field.name ==
             'insurance_duration' else field.value_to_string(self))
            for field in Car._meta.fields
            if field.name not in ["owner", "id", "make", "model"]
        ]

    def get_absolute_url(self):
        return reverse("maintenance:car-detail", args=[str(self.id)])

    def __str__(self):
        return f'{self.make} {self.model}'

# Generated by Django 3.1.2 on 2020-10-30 08:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('maintenance', '0003_auto_20201026_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='insurance_duration',
            field=models.CharField(choices=[('12', 'rok'), ('6', 'pół roku'), ('3', 'trzy miesiące'), ('1', 'miesiąc')], max_length=2, verbose_name='Czas trwania umowy OC'),
        ),
        migrations.AlterField(
            model_name='car',
            name='last_inspection',
            field=models.DateField(verbose_name='Data ostatniego przeglądu'),
        ),
        migrations.AlterField(
            model_name='car',
            name='last_insurance',
            field=models.DateField(verbose_name='Data zawarcia ostatniej umowy OC'),
        ),
        migrations.AlterField(
            model_name='car',
            name='make',
            field=models.CharField(max_length=64, verbose_name='Marka'),
        ),
        migrations.AlterField(
            model_name='car',
            name='mileage',
            field=models.PositiveIntegerField(verbose_name='Przebieg'),
        ),
        migrations.AlterField(
            model_name='car',
            name='model',
            field=models.CharField(max_length=64, verbose_name='Model'),
        ),
        migrations.AlterField(
            model_name='car',
            name='oil_service_date_last_done',
            field=models.DateField(verbose_name='Data ostatniej wymiany oleju'),
        ),
        migrations.AlterField(
            model_name='car',
            name='oil_service_interval',
            field=models.PositiveSmallIntegerField(verbose_name='Interwał wymiany oleju'),
        ),
        migrations.AlterField(
            model_name='car',
            name='oil_service_mileage_last_done',
            field=models.PositiveIntegerField(verbose_name='Przebieg przy ostatniej wymianie oleju'),
        ),
        migrations.AlterField(
            model_name='car',
            name='oil_service_oil_type',
            field=models.CharField(max_length=128, verbose_name='Rodzaj oleju'),
        ),
        migrations.AlterField(
            model_name='car',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Właściciel'),
        ),
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.DateField(verbose_name='Rok produkcji'),
        ),
    ]

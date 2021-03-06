# Generated by Django 3.1.2 on 2020-10-26 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OilService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interval', models.PositiveSmallIntegerField()),
                ('date_last_done', models.DateField()),
                ('mileage_last_done', models.PositiveIntegerField()),
                ('oil_type', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=64)),
                ('model', models.CharField(max_length=64)),
                ('year', models.DateField()),
                ('mileage', models.PositiveIntegerField()),
                ('last_inspection', models.DateField()),
                ('last_insurance', models.DateField()),
                ('insurance_duration', models.CharField(choices=[('Y', 'one year'), ('6M', 'six months'), ('3M', 'three months')], max_length=2)),
                ('oil_service', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='maintenance.oilservice')),
            ],
        ),
    ]

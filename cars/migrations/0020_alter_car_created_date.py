# Generated by Django 4.0 on 2023-07-03 12:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0019_alter_car_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 7, 3, 15, 29, 46, 803860)),
        ),
    ]

# Generated by Django 4.1.3 on 2023-04-14 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parcels', '0006_ride_destination'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='status',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]

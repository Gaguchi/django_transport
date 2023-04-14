# Generated by Django 4.1.3 on 2023-03-25 10:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_location', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100, null=True)),
                ('start_date', models.DateField(null=True)),
                ('arrival_date', models.DateField(null=True)),
                ('status', models.CharField(choices=[('P', 'Planned'), ('O', 'On going'), ('C', 'Completed')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Parcel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tracking_number', models.CharField(max_length=50)),
                ('delivery_address', models.CharField(max_length=100)),
                ('assigned_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('travel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parcels', to='parcels.travel')),
            ],
        ),
    ]
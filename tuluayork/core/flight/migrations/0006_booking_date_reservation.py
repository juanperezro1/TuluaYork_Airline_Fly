# Generated by Django 3.1.6 on 2021-03-16 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0005_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='date_reservation',
            field=models.DateField(default='2021-03-16'),
        ),
    ]

# Generated by Django 3.1.6 on 2021-03-05 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0003_auto_20210305_1612'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flight',
            name='requirements',
        ),
        migrations.AddField(
            model_name='flight',
            name='requirements',
            field=models.ManyToManyField(to='flight.requirement'),
        ),
    ]
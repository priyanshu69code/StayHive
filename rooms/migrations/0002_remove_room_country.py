# Generated by Django 5.0.1 on 2024-02-05 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='country',
        ),
    ]

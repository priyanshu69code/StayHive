# Generated by Django 5.0.1 on 2024-02-11 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0003_roomphotos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomphotos',
            name='img',
            field=models.ImageField(upload_to='roomsphotos'),
        ),
    ]
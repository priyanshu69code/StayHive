# Generated by Django 5.0.4 on 2024-04-23 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0004_alter_review_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='review',
            field=models.TextField(max_length=1000),
        ),
    ]

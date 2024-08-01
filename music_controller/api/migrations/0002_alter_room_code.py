# Generated by Django 4.2.14 on 2024-07-18 21:57

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='code',
            field=models.CharField(default=api.models.create_unique_code, max_length=10, unique=True),
        ),
    ]

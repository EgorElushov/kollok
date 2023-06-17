# Generated by Django 4.2.2 on 2023-06-17 09:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='count',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
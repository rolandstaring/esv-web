# Generated by Django 4.0.6 on 2023-01-03 15:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esv', '0018_countryrules'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countryrules',
            name='saldering',
            field=models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)]),
        ),
        migrations.AlterField(
            model_name='heatpump',
            name='gbc',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)]),
        ),
        migrations.AlterField(
            model_name='solarpannels',
            name='schaduw_factor',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)]),
        ),
    ]

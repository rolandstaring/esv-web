# Generated by Django 4.0.6 on 2022-12-15 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('esv', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='house',
            old_name='eigenaar',
            new_name='bewoner',
        ),
    ]

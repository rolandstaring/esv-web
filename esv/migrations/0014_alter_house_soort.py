# Generated by Django 4.0.6 on 2022-12-29 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esv', '0013_scenariomodel_insulation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='soort',
            field=models.CharField(choices=[('hoekwoning', 'Hoekwoning'), ('tussenwoning', 'Tussenwoning'), ('2onder1kap', '2-onder-1-kap'), ('vrijstaand', 'Vrij staand')], default='tussenwoning', max_length=14),
        ),
    ]

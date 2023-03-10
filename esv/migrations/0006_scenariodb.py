# Generated by Django 4.0.6 on 2022-12-21 22:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('esv', '0005_appliance_heatpump_homebattery_solarboiler_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScenarioDB',
            fields=[
                ('naam', models.CharField(max_length=30)),
                ('house', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='esv.house')),
                ('heatpump', models.ManyToManyField(to='esv.heatpump')),
                ('solarboilers', models.ManyToManyField(to='esv.solarboiler')),
                ('solarpannels', models.ManyToManyField(to='esv.solarpannels')),
            ],
        ),
    ]

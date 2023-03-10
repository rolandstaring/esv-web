# Generated by Django 4.0.6 on 2022-12-23 23:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('esv', '0009_scenariodb_id_alter_scenariodb_house'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScenarioModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naam', models.CharField(max_length=30)),
                ('saldering', models.FloatField(default=1)),
                ('eigenaar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('heatpump', models.ManyToManyField(to='esv.heatpump')),
                ('house', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='esv.house')),
                ('solarboilers', models.ManyToManyField(to='esv.solarboiler')),
                ('solarpannels', models.ManyToManyField(to='esv.solarpannels')),
            ],
        ),
        migrations.DeleteModel(
            name='ScenarioDB',
        ),
    ]

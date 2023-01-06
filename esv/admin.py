from django.contrib import admin
from .models import House, Solarpannels,Solarboiler,Heatpump,Homebattery,ScenarioModel, CountryRules

admin.site.register(House)
admin.site.register(Solarpannels)
admin.site.register(Solarboiler)
admin.site.register(Heatpump)
admin.site.register(Homebattery)
admin.site.register(ScenarioModel)
admin.site.register(CountryRules)
# Register your models here.

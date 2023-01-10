from django.conf import settings
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


HOUSE_CHOICES = (('hoekwoning', 'Hoekwoning'),
                ('tussenwoning', 'Tussenwoning'),
                ('2onder1kap', '2-onder-1-kap'),
                ('vrijstaand','Vrij staand'),)

INSULATION_CHOICES = (('dakisolatie', 'Dakisolatie'),
                    ('vloerisolatie', 'Vloerisolatie'),
                    ('spouwisolatie', 'Spouwisolatie'),
                    ('glasisolatie','Glasisolatie'),)


# Create your models here.
class House(models.Model):
    bewoner= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    naam = models.CharField(max_length=200)
    soort = models.CharField(max_length=14, choices=HOUSE_CHOICES, default='tussenwoning')
    gas_verbruik = models.IntegerField()
    stroom_verbruik = models.IntegerField()
    gas_prijs_var= models.FloatField()
    stroom_prijs_var = models.FloatField()
    stroom_lever_prijs_var = models.FloatField()
    gas_prijs_vast_dag= models.FloatField()
    stroom_prijs_vast_dag = models.FloatField()

    def __str__(self):
        return self.naam


class Insulation(models.Model):
    eigenaar= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    soort = models.CharField(max_length=14, choices=INSULATION_CHOICES, default='vloerisolatie')
    naam = models.CharField(max_length=200)
    prijs = models.IntegerField()
    rd = models.FloatField()
    m2 = models.IntegerField()

    def __str__(self):
        return self.naam

class Appliance(models.Model):
    eigenaar= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    naam = models.CharField(max_length=200)
    prijs = models.IntegerField()

    def __str__(self):
        return self.naam

class Solarpannels(Appliance):
    watt_cap_pp = models.IntegerField()
    aantal = models.IntegerField()
    jaar_van_aanschaf = models.IntegerField()
    schaduw_factor = models.FloatField(validators=[MinValueValidator(0.0),
                                       MaxValueValidator(1.0)])

class Solarboiler(Appliance):
    watt = models.IntegerField()
    watt_cap = models.IntegerField()

class Heatpump(Appliance):
    cop = models.FloatField()
    watt_cap = models.IntegerField()
    gbc = models.FloatField(validators=[MinValueValidator(0.0),
                                       MaxValueValidator(1.0)])

class Homebattery(Appliance):
    watt_cap = models.IntegerField()

class CountryRules(models.Model):
    eigenaar= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    gas_prijs_plafond = models.FloatField()
    stroom_prijs_plafond = models.FloatField()
    gas_plafond = models.IntegerField()
    stroom_plafond = models.IntegerField()
    saldering = models.FloatField(default=1, validators=[MinValueValidator(0.0),
                                       MaxValueValidator(1.0)])

class ScenarioModel(models.Model):
    eigenaar= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    naam = models.CharField(max_length=30)
    plafond = models.BooleanField(default=False)
    solarpannels = models.ManyToManyField(Solarpannels)
    solarboilers =  models.ManyToManyField(Solarboiler)
    heatpump =  models.ManyToManyField(Heatpump)
    homebattery =  models.ManyToManyField(Homebattery)
    insulation = models.ManyToManyField(Insulation)
    maandbedrag = models.IntegerField(default=0)
    gasverbruik_na = models.IntegerField(default=0)
    stroomverbruik_na = models.IntegerField(default=0)

    def __str__(self):
        return self.naam




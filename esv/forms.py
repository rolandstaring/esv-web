from django import forms
from .models import House, Solarpannels,Solarboiler,Heatpump,Homebattery, Insulation, ScenarioModel, CountryRules
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from datetime import date

# authentication form

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class CountryRulesForm(forms.ModelForm):

    class Meta:
        model = CountryRules
        fields = ('gas_prijs_plafond',
                    'stroom_prijs_plafond',
                    'gas_plafond',
                    'stroom_plafond',
                    'saldering')


class HouseForm(forms.ModelForm):

    class Meta:
        model = House
        fields = ('naam',
                'soort',
                'gas_verbruik',
                'stroom_verbruik',
                'gas_prijs_var',
                'stroom_prijs_var',
                'stroom_lever_prijs_var',
                'gas_prijs_vast_dag',
                'stroom_prijs_vast_dag')



class InsulationForm(forms.ModelForm):

    class Meta:
        model = Insulation
        fields = ('soort',
                'naam',
                'prijs',
                'rd',
                'm2')

class SolarpannelsForm(forms.ModelForm):

    class Meta:
        model = Solarpannels
        fields = ('naam',
                'prijs',
                'watt_cap_pp',
                'aantal',
                'jaar_van_aanschaf',
                'schaduw_factor')

        labels = {'prijs' : 'Prijs (alle panelen) ',
                    'watt_cap_pp':'Watt piek per paneel',
                        'aantal':'Aantal panelen',
                        'jaar_van_aanschaf':'Jaar waarin het paneel gekocht is en aangesloten',
                        'schaduw_factor':'Getal tussen 0 en 1. Waarbij 1 is geen schaduw en 0 alleen maar schaduw'}

class SolarboilerForm(forms.ModelForm):

    class Meta:
        model = Solarboiler
        fields = ('naam',
                'prijs',
                'watt',
                'watt_cap')
        labels ={'watt' : 'Hoeveel watt verbruikt de pomp van de Zonneboiler',
                'watt_cap' : 'Verwachte jaarlijkse energie opbrengst (in kwh per jaar)',}

class HeatpumpForm(forms.ModelForm):

    class Meta:
        model = Heatpump
        fields = ('naam',
                'prijs',
                'cop',
                'gbc')
        labels = {'cop' : 'Gemiddelde rendement van de warmtepomp. Hoe hoger hoe beter. Meestal rond de 4',
                        'gbc' : 'Gas besparings coefficient. Bij 1 verwacht je alle gas te kunnen besparen en bij 0 geen',}

class HomebatteryForm(forms.ModelForm):

    class Meta:
        model = Homebattery
        fields = ('naam',
                'prijs',
                'watt_cap')
        labels = {'watt_cap' : 'Hoeveel energie kan de batterij opslaan in kwh',}

class ScenariocompareForm(forms.Form):
    ist = forms.ModelChoiceField(queryset=ScenarioModel.objects.all(), widget=forms.RadioSelect)
    soll = forms.ModelChoiceField(queryset=ScenarioModel.objects.all(), widget=forms.RadioSelect)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(ScenariocompareForm, self).__init__(*args, **kwargs)
        self.fields['ist'].label = 'Huidige scenaro'
        self.fields['ist'].queryset = ScenarioModel.objects.filter(eigenaar=self.request.user)
        self.fields['soll'].label = 'Toekomst scenario'
        self.fields['soll'].queryset = ScenarioModel.objects.filter(eigenaar=self.request.user)

class ScenarioselectForm(forms.Form):
    name = forms.CharField(label = 'Naam')
    plafond = forms.BooleanField(required = False, label ='Plafond' )
    houseList = forms.ModelChoiceField(queryset =House.objects.all(),widget=forms.RadioSelect)
    solarpannelsList = forms.ModelMultipleChoiceField(queryset = Solarpannels.objects.all(), widget=forms.CheckboxSelectMultiple,required=False)
    solarboilerList = forms.ModelMultipleChoiceField (queryset =Solarboiler.objects.all(), widget=forms.CheckboxSelectMultiple,required=False)
    heatpumpList = forms.ModelMultipleChoiceField(queryset = Heatpump.objects.all(), widget=forms.CheckboxSelectMultiple,required=False)
    homebatteryList = forms.ModelMultipleChoiceField(queryset = Homebattery.objects.all(), widget=forms.CheckboxSelectMultiple,required=False)
    insulationList = forms.ModelMultipleChoiceField(queryset = Insulation.objects.all(), widget=forms.CheckboxSelectMultiple,required=False)

    def __init__(self, *args, **kwargs):

        self.request = kwargs.pop('request')
        super(ScenarioselectForm, self).__init__(*args, **kwargs)
        self.fields['houseList'].label = 'Huis waarop het scenario van toepassing is'
        self.fields['houseList'].queryset = House.objects.filter(bewoner=self.request.user)
        self.fields['solarpannelsList'].label = 'Zonnepanelen'
        self.fields['solarpannelsList'].queryset = Solarpannels.objects.filter(eigenaar=self.request.user)
        self.fields['solarboilerList'].label = 'Zonneboiler'
        self.fields['solarboilerList'].queryset = Solarboiler.objects.filter(eigenaar=self.request.user)
        self.fields['heatpumpList'].label = 'Warmtepomp'
        self.fields['heatpumpList'].queryset = Heatpump.objects.filter(eigenaar=self.request.user)
        self.fields['homebatteryList'].label = 'Thuisbatterij'
        self.fields['homebatteryList'].queryset = Homebattery.objects.filter(eigenaar=self.request.user)
        self.fields['insulationList'].label = 'Isolatie'
        self.fields['insulationList'].queryset = Insulation.objects.filter(eigenaar=self.request.user)





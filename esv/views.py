from django.shortcuts import render, redirect, get_object_or_404
from .models import House, Solarpannels, Solarboiler, Heatpump, ScenarioModel, Insulation, Homebattery,CountryRules
from .forms import HouseForm, SolarpannelsForm, SolarboilerForm, HeatpumpForm, ScenarioselectForm, InsulationForm, ScenariocompareForm,NewUserForm, HomebatteryForm, CountryRulesForm
from .scenario import ScenarioZonderPlafond, ScenarioMetPlafond, VergelijkScenarios
from .huis import Huishouden, EnergieVerbruik, EnergiePrijs, Plafond
from .apparaat import Zonnepanelen, Zonneboiler, Warmtepomp, Thuisbatterij
from .report import Report
from .isolatie import Vloerisolatie,Dakisolatie, Spouwisolatie, Glasisolatie
from django.contrib.auth import login,logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from datetime import date


def render_home_page(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.user:
        insulations = Insulation.objects.filter(eigenaar = request.user)
        houses = House.objects.filter(bewoner = request.user)
        solarpannels = Solarpannels.objects.filter(eigenaar = request.user)
        solarboilers = Solarboiler.objects.filter(eigenaar = request.user)
        heatpumps = Heatpump.objects.filter(eigenaar = request.user)
        homebatteries = Homebattery.objects.filter(eigenaar = request.user)
        scenarios = ScenarioModel.objects.filter(eigenaar = request.user)
        countryrules = CountryRules.objects.filter(eigenaar = request.user)

        if countryrules:
            pass
        else:
            add_templates(request)

        view_list = {'houses':houses,
                'solarpannels':solarpannels,
                'solarboilers':solarboilers,
                'heatpumps':heatpumps,
                'scenarios': scenarios,
                'homebatteries': homebatteries,
                'insulations': insulations,
                'countryrules': countryrules}

        return render(request, 'esv/house_list.html', view_list)

def add_template_country(request):
    country_rules = CountryRules.objects.create( eigenaar = request.user,
                        gas_prijs_plafond = '1.45',
                        stroom_prijs_plafond = '0.4',
                        gas_plafond = '1200',
                        stroom_plafond = '2900')
    country_rules.save()

def add_templates_solarpannels(request):
    solar_small = Solarpannels.objects.create(eigenaar = request.user,
                    naam = '4 panelen 375w',
                    prijs = '3000',
                    watt_cap_pp = '375',
                    aantal = '4',
                    jaar_van_aanschaf = str(date.today().year),
                    schaduw_factor = '0.8')
    solar_middle = Solarpannels.objects.create(eigenaar = request.user,
                    naam = '8 panelen 375w',
                    prijs = '6000',
                    watt_cap_pp = '375',
                    aantal = '8',
                    jaar_van_aanschaf = str(date.today().year),
                    schaduw_factor = '0.8')
    solar_high = Solarpannels.objects.create( eigenaar = request.user,
                    naam = '12 panelen 375w',
                    prijs = '8000',
                    watt_cap_pp = '375',
                    aantal = '12',
                    jaar_van_aanschaf = str(date.today().year),
                    schaduw_factor = '0.8')
    solar_small.save()
    solar_middle.save()
    solar_high.save()

def add_templates_heatpumps(request):
    heatpump_small = Heatpump.objects.create(eigenaar = request.user,
                    naam = 'Hybride klein',
                    prijs = '2500',
                    cop = '4.9',
                    watt_cap = '4400',
                    gbc = '0.8')
    heatpump_middle = Heatpump.objects.create(eigenaar = request.user,
                    naam = 'Hybride groot',
                    prijs = '3500',
                    cop = '4.9',
                    watt_cap = '8000',
                    gbc = '0.9')
    heatpump_high = Heatpump.objects.create(eigenaar = request.user,
                    naam = 'All electric',
                    prijs = '5000',
                    cop = '4.9',
                    watt_cap = '12000',
                    gbc = '1')

    heatpump_small.save()
    heatpump_middle.save()
    heatpump_high.save()

def add_templates_solarboilers(request):
    sb_small = Solarboiler.objects.create(eigenaar = request.user,
                    naam = '2 personen zonneboiler',
                    prijs = '3000',
                    watt = '60',
                    watt_cap = '1340',
                    )
    sb_middle = Solarboiler.objects.create(eigenaar = request.user,
                    naam = '4 personen zonneboiler',
                    prijs = '4500',
                    watt = '60',
                    watt_cap = '2340',
                    )
    sb_high = Solarboiler.objects.create( eigenaar = request.user,
                    naam = '6 personen zonneboiler',
                    prijs = '6500',
                    watt = '60',
                    watt_cap = '3295',
                    )
    sb_small.save()
    sb_middle.save()
    sb_high.save()

def add_templates_homebattery(request):
    hb_small = Homebattery.objects.create(eigenaar = request.user,
                    naam = 'Batterij 3kwh',
                    prijs = '3500',
                    watt_cap = '4000',
                    )
    hb_middle = Homebattery.objects.create(eigenaar = request.user,
                    naam = 'Batterij 6kwh ',
                    prijs = '5000',
                    watt_cap = '6000',
                    )
    hb_high = Homebattery.objects.create( eigenaar = request.user,
                    naam = 'Batterij 10kwh',
                    prijs = '10000',
                    watt_cap = '10000',
                    )
    hb_small.save()
    hb_middle.save()
    hb_high.save()


def add_templates(request):
    add_template_country(request)
    add_templates_solarpannels(request)
    add_templates_solarboilers(request)
    add_templates_heatpumps(request)
    add_templates_homebattery(request)





def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("house_list")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="esv/register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("house_list")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="esv/login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.")
	return redirect("house_list")


# Create your views here.
def house_list(request):
    return render_home_page(request)


##################################
##### Country Rules new, edit ####
##################################

def country_edit(request, pk):
    country_rules = get_object_or_404(CountryRules, pk=pk)
    if request.method == "POST":
        form = CountryRulesForm(request.POST, instance=country_rules)
        if form.is_valid():
            country_rules = form.save(commit=False)
            country_rules.eigenaar = request.user
            country_rules.save()
            return render_home_page(request)
    else:
        form = CountryRulesForm(instance=country_rules)
    return render(request, 'esv/country_edit.html', {'form': form})






##################################
##### House new,edit #############
##################################



def house_new(request):
    if request.method == "POST":
        form = HouseForm(request.POST)
        if form.is_valid():
            house = form.save(commit=False)
            house.bewoner = request.user
            house.save()
            return render_home_page(request)
    else:
        form = HouseForm()
    return render(request, 'esv/house_edit.html', {'form': form})


def house_edit(request, pk):
    house = get_object_or_404(House, pk=pk)
    if request.method == "POST":
        form = HouseForm(request.POST, instance=house)
        if form.is_valid():
            house = form.save(commit=False)
            house.bewoner = request.user
            house.save()
            return render_home_page(request)
    else:
        form = HouseForm(instance=house)
    return render(request, 'esv/house_edit.html', {'form': form})

def house_del(request, pk):
    House.objects.filter(pk=pk).delete()
    return render_home_page(request)

##################################
##### Solarpannels new,edit ######
##################################


def solarpannels_edit(request, pk):
    solarpannels = get_object_or_404(Solarpannels, pk=pk)
    if request.method == "POST":
        form = SolarpannelsForm(request.POST, instance=solarpannels)
        if form.is_valid():
            solarpannels = form.save(commit=False)
            solarpannels.eigenaar = request.user
            solarpannels.save()
            return render_home_page(request)
    else:
        form = SolarpannelsForm(instance=solarpannels)
    return render(request, 'esv/solarpannels_edit.html', {'form': form})

def solarpannels_new(request):
    if request.method == "POST":
        form = SolarpannelsForm(request.POST)
        if form.is_valid():
            solarpannels = form.save(commit=False)
            solarpannels.eigenaar = request.user
            solarpannels.save()
            return render_home_page(request)
    else:
        form = SolarpannelsForm(initial = {
                    'jaar_van_aanschaf' : str(date.today().year) ,
                    'schaduw_factor' : '0.8'})
    return render(request, 'esv/solarpannels_edit.html', {'form': form})

def solarpannels_del(request, pk):
    Solarpannels.objects.filter(pk=pk).delete()
    return render_home_page(request)

##################################
##### Solarboiler new,edit  ######
##################################

def solarboiler_edit(request, pk):
    solarboiler = get_object_or_404(Solarboiler, pk=pk)
    if request.method == "POST":
        form = SolarboilerForm(request.POST, instance=solarboiler)
        if form.is_valid():
            solarboiler = form.save(commit=False)
            solarboiler.eigenaar = request.user
            solarboiler.save()
            return render_home_page(request)
    else:
        form = SolarboilerForm(instance=solarboiler)
    return render(request, 'esv/solarboiler_edit.html', {'form': form})

def solarboiler_new(request):
    if request.method == "POST":
        form = SolarboilerForm(request.POST)
        if form.is_valid():
            solarboiler = form.save(commit=False)
            solarboiler.eigenaar = request.user
            solarboiler.save()
            return render_home_page(request)
    else:
        form = SolarboilerForm()
    return render(request, 'esv/solarboiler_edit.html', {'form': form})

def solarboiler_del(request, pk):
    Solarboiler.objects.filter(pk=pk).delete()
    return render_home_page(request)

##################################
##### Homebattery new,edit     ###
##################################


def homebattery_edit(request, pk):
    homebattery = get_object_or_404(Homebattery, pk=pk)
    if request.method == "POST":
        form = HomebatteryForm(request.POST, instance=homebattery)
        if form.is_valid():
            homebattery = form.save(commit=False)
            homebattery.eigenaar = request.user
            homebattery.save()
            return render_home_page(request)
    else:
        form = HomebatteryForm(instance=homebattery)
    return render(request, 'esv/homebattery_edit.html', {'form': form})

def homebattery_new(request):
    if request.method == "POST":
        form = HomebatteryForm(request.POST)
        if form.is_valid():
            homebattery = form.save(commit=False)
            homebattery.eigenaar = request.user
            homebattery.save()
            return render_home_page(request)
    else:
        form = HomebatteryForm()
    return render(request, 'esv/homebattery_edit.html', {'form': form})


def homebattery_del(request, pk):
    Homebattery.objects.filter(pk=pk).delete()
    return render_home_page(request)


##################################
##### Heatpump new,edit     ######
##################################


def heatpump_edit(request, pk):
    heatpump = get_object_or_404(Heatpump, pk=pk)
    if request.method == "POST":
        form = HeatpumpForm(request.POST, instance=heatpump)
        if form.is_valid():
            heatpump = form.save(commit=False)
            heatpump.eigenaar = request.user
            heatpump.save()
            return render_home_page(request)
    else:
        form = HeatpumpForm(instance=heatpump)
    return render(request, 'esv/heatpump_edit.html', {'form': form})

def heatpump_new(request):
    if request.method == "POST":
        form = HeatpumpForm(request.POST)
        if form.is_valid():
            heatpump = form.save(commit=False)
            heatpump.eigenaar = request.user
            heatpump.save()
            return render_home_page(request)
    else:
        form = HeatpumpForm()
    return render(request, 'esv/heatpump_edit.html', {'form': form})


def heatpump_del(request, pk):
    Heatpump.objects.filter(pk=pk).delete()
    return render_home_page(request)

##################################
##### Isolatie new,edit     ######
##################################

def insulation_edit(request, pk):
    insulation = get_object_or_404(Insulation, pk=pk)
    if request.method == "POST":
        form = InsulationForm(request.POST, instance=insulation)
        if form.is_valid():
            insulation = form.save(commit=False)
            insulation.eigenaar = request.user
            insulation.save()
            return render_home_page(request)
    else:
        form = InsulationForm(instance=insulation)
    return render(request, 'esv/insulation_edit.html', {'form': form})

def insulation_new(request):
    if request.method == "POST":
        form =InsulationForm(request.POST)
        if form.is_valid():
            heatpump = form.save(commit=False)
            heatpump.eigenaar = request.user
            heatpump.save()
            return render_home_page(request)
    else:
        form = InsulationForm()
    return render(request, 'esv/insulation_edit.html', {'form': form})

def insulation_del(request, pk):
    Insulation.objects.filter(pk=pk).delete()
    return render_home_page(request)

##################################
##### Scenario run, make, edit ###
##################################

def save_scenario(scenario_eigenaar,scenario_name,scenario_plafond, choice_house, choices_solarpannels, choices_solarboilers, choices_heatpumps,choices_homebatteries, choices_insulation):


    scenariodb = ScenarioModel()
    scenariodb.naam = scenario_name
    scenariodb.eigenaar = scenario_eigenaar
    scenariodb.plafond = scenario_plafond
    scenariodb.house = House.objects.get(pk = choice_house)
    scenariodb.save()


    for choice in choices_solarpannels:
        sp = Solarpannels.objects.get(pk = int(choice))
        scenariodb.solarpannels.add(sp)

    for choice in choices_solarboilers:
        sb = Solarboiler.objects.get(pk = int(choice))
        scenariodb.solarboilers.add(sb)

    for choice in choices_heatpumps:
        hp = Heatpump.objects.get(pk = int(choice))
        scenariodb.heatpump.add(hp)

    for choice in choices_insulation:
        hp = Insulation.objects.get(pk = int(choice))
        scenariodb.insulation.add(hp)

    for choice in choices_homebatteries:
        hp = Homebattery.objects.get(pk = int(choice))
        scenariodb.homebattery.add(hp)

    scenario = make_scenario(scenario_eigenaar,
                            scenariodb.naam,
                            scenariodb.plafond,
                            scenariodb.house,
                            scenariodb.solarpannels,
                            scenariodb.solarboilers,
                            scenariodb.heatpump,
                            scenariodb.homebattery,
                            scenariodb.insulation)
    scenariodb.maandbedrag = scenario.kosten.totaal_kosten_maand()

    scenariodb.gasverbruik_na = scenario.verbruik_na.gas_verbruik_jaar
    scenariodb.stroomverbruik_na = scenario.verbruik_na.stroom_verbruik_jaar
    scenariodb.save(update_fields=['maandbedrag'])
    scenariodb.save(update_fields=['stroomverbruik_na'])
    scenariodb.save(update_fields=['gasverbruik_na'])

def make_scenario(scenario_eigenaar,scenario_name,scenario_plafond, house, choices_solarpannels, choices_solarboilers, choices_heatpumps,choices_homebatteries, choices_insulation):

    countryrule = CountryRules.objects.filter(eigenaar = scenario_eigenaar).first()

    prijzen = EnergiePrijs(house.gas_prijs_var,house.stroom_prijs_var, house.stroom_lever_prijs_var,house.stroom_prijs_vast_dag,house.gas_prijs_vast_dag)
    verbruik = EnergieVerbruik('Huidig Verbruik',house.gas_verbruik,house.stroom_verbruik)
    huis = Huishouden(house.naam, house.soort, verbruik, prijzen, float(countryrule.saldering))

    app_l = []
    ins_l = []

    for solarpannels in choices_solarpannels.all():
        zonnepanelen = Zonnepanelen(solarpannels.naam, solarpannels.prijs, solarpannels.watt_cap_pp, solarpannels.aantal, solarpannels.jaar_van_aanschaf, solarpannels.schaduw_factor)
        app_l.append(zonnepanelen)

    for solarboiler in choices_solarboilers.all():
        zonneboiler = Zonneboiler(solarboiler.naam, solarboiler.prijs, solarboiler.watt_cap, solarboiler.watt)
        app_l.append(zonneboiler)

    for heatpump in choices_heatpumps.all():
        warmtepomp = Warmtepomp(heatpump.naam, heatpump.prijs, heatpump.cop, heatpump.gbc)
        app_l.append(warmtepomp)

    for homebattery in choices_homebatteries.all():
        thuisbatterij = Thuisbatterij(homebattery.naam, homebattery.prijs, homebattery.watt_cap)
        app_l.append(thuisbatterij)

    for insulation in choices_insulation.all():
        if insulation.soort=='vloerisolatie':
            vloerisolatie = Vloerisolatie(insulation.naam, insulation.prijs, insulation.rd,insulation.m2)
            ins_l.append(vloerisolatie)
        elif insulation.soort=='dakisolatie':
            dakisolatie = Dakisolatie(insulation.naam, insulation.prijs, insulation.rd,insulation.m2)
            ins_l.append(dakisolatie)
        elif insulation.soort=='spouwisolatie':
            spouwisolatie = Spouwisolatie(insulation.naam, insulation.prijs, insulation.rd,insulation.m2)
            ins_l.append(spouwisolatie)
        elif insulation.soort == 'glasisolatie':
            glasisolatie = Glasisolatie(insulation.naam, insulation.prijs, insulation.rd,insulation.m2)
            ins_l.append(glasisolatie)

    if scenario_plafond == True:

        plafond_prijzen = EnergiePrijs(countryrule.gas_prijs_plafond, countryrule.stroom_prijs_plafond)
        plafond = Plafond(plafond_prijzen, countryrule.gas_plafond,countryrule.stroom_plafond)
        return ScenarioMetPlafond(scenario_name, ins_l, app_l, huis, plafond)
    else:
        return ScenarioZonderPlafond(scenario_name, ins_l , app_l, huis)

def scenario_del(request, pk):
    ScenarioModel.objects.filter(pk=pk).delete()
    return render_home_page(request)


def scenario_run(request,pk):
    scenario_model = get_object_or_404(ScenarioModel, pk=pk)

    scenario = make_scenario(request.user,
                            scenario_model.naam,
                            scenario_model.plafond,
                            scenario_model.house,
                            scenario_model.solarpannels,
                            scenario_model.solarboilers,
                            scenario_model.heatpump,
                            scenario_model.homebattery,
                            scenario_model.insulation)

    #display results of scenario
    report = Report(scenario)
    input_scenario = report.input_berekeningen()
    output_scenario = report.output_berekeningen()
    stroom_scenario = report.stroom_berekeningen()
    gas_scenario = report.gas_berekeningen()

    return render(request, 'esv/scenario_print.html', {'input_scenario': input_scenario,
                                                            'output_scenario': output_scenario,
                                                            'stroom_scenario': stroom_scenario,
                                                            'gas_scenario': gas_scenario,
                                                            })
def scenario_new(request):
    if request.method == "POST":
        form = ScenarioselectForm(request.POST, request = request)
        if form.is_valid():
            choice_house = form['houseList'].data
            scenario_name = form['name'].data
            scenario_plafond = form['plafond'].data
            choices_solarpannels = form['solarpannelsList'].value()
            choices_solarboilers = form['solarboilerList'].value()
            choices_heatpumps = form['heatpumpList'].value()
            choices_homebatteries = form['homebatteryList'].value()
            choices_insulation = form['insulationList'].value()
            scenario_eigenaar = request.user
            save_scenario(scenario_eigenaar,
                            scenario_name,
                            scenario_plafond,
                            choice_house,
                            choices_solarpannels,
                            choices_solarboilers,
                            choices_heatpumps,
                            choices_homebatteries,
                            choices_insulation)
            return render_home_page(request)

    else:
        form = ScenarioselectForm(request = request )
    return render(request, 'esv/scenario_edit.html', {'form': form})

#{'user': request.user}

def scenariocompare_new(request):
    if request.method == "POST":
        form = ScenariocompareForm(request.POST, request = request)
        if form.is_valid():
            ist_scenario_pk = form['ist'].data
            soll_scenario_pk = form['soll'].data
            ist_scenario = ScenarioModel.objects.get(pk = ist_scenario_pk)
            soll_scenario = ScenarioModel.objects.get(pk = soll_scenario_pk)

            huidig = make_scenario(request.user,
                                    ist_scenario.naam,
                                    ist_scenario.plafond,
                                    ist_scenario.house,
                                    ist_scenario.solarpannels,
                                    ist_scenario.solarboilers,
                                    ist_scenario.heatpump,
                                    ist_scenario.homebattery,
                                    ist_scenario.insulation
                                    )

            toekomst = make_scenario(request.user,
                                    soll_scenario.naam,
                                    soll_scenario.plafond,
                                    soll_scenario.house,
                                    soll_scenario.solarpannels,
                                    soll_scenario.solarboilers,
                                    soll_scenario.heatpump,
                                    soll_scenario.homebattery,
                                    soll_scenario.insulation)

            kosten_huidig = huidig.kosten.print_html()
            kosten_toekomst = toekomst.kosten.print_html()

            vergelijk_scenarios = VergelijkScenarios(huidig, toekomst)
            roi = vergelijk_scenarios.print_html()
            complement = vergelijk_scenarios.print_complement_html()
            return render(request, 'esv/scenariocompare_print.html', {'kosten_huidig': kosten_huidig,
                                                                        'kosten_toekomst': kosten_toekomst,
                                                                        'complement': complement,
                                                                        'roi': roi})

    else:
        form = ScenariocompareForm(request = request)
    return render(request, 'esv/scenariocompare_edit.html', {'form': form})






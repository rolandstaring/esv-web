from django.urls import path
from . import views



urlpatterns = [
    path('', views.house_list, name='house_list'),
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name= "logout"),

    path('country/<int:pk>', views.country_edit, name='country_edit'),

    path('house/<int:pk>/edit/', views.house_edit, name='house_edit'),
    path('house/<int:pk>', views.house_del, name='house_del'),
    path('house/new/', views.house_new, name='house_new'),

    path('scenariocompare/new/', views.scenariocompare_new, name='scenariocompare_new'),

    path('scenario/new/', views.scenario_new, name='scenario_new'),
    path('scenario/<int:pk>/', views.scenario_run, name='scenario_run'),
    path('scenario/<int:pk>', views.scenario_del, name='scenario_del'),

    path('insulation/<int:pk>/edit/', views.insulation_edit, name='insulation_edit'),
    path('insulation/new/', views.insulation_new, name='insulation_new'),
    path('insulation/<int:pk>', views.insulation_del, name='insulation_del'),

    path('solarpannels/<int:pk>/edit/', views.solarpannels_edit, name='solarpannels_edit'),
    path('solarpannels/new/', views.solarpannels_new, name='solarpannels_new'),
    path('solarpannels/<int:pk>', views.solarpannels_del, name='solarpannels_del'),

    path('solarboiler/<int:pk>/edit/', views.solarboiler_edit, name='solarboiler_edit'),
    path('solarboiler/new/', views.solarboiler_new, name='solarboiler_new'),
    path('solarboiler/<int:pk>', views.solarboiler_del, name='solarboiler_del'),

    path('homebattery/<int:pk>/edit/', views.homebattery_edit, name='homebattery_edit'),
    path('homebattery/new/', views.homebattery_new, name='homebattery_new'),
    path('homebattery/<int:pk>', views.homebattery_del, name='homebattery_del'),

    #path('heatpump/<int:pk>/', views.heatpump_detail, name='heatpump_detail'),
    path('heatpump/<int:pk>/edit/', views.heatpump_edit, name='heatpump_edit'),
    path('heatpump/new/', views.heatpump_new, name='heatpump_new'),
    path('heatpump/<int:pk>', views.heatpump_del, name='heatpump_del'),


]
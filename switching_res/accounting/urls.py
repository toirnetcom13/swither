from django.urls import path

from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('substation_jur/<int:name_of_substation_id>/', substation_jur, name='substation_jur'),
    path('branch_jur/<int:branch_id>/', branch_jur, name='branch_jur'),
    path('circuit_breakers_jur/', circuit_breakers_jur, name='circuit_breakers_jur'),
    path('Breakers_branch_jur/<int:branch_id>/', breakers_branch_jur, name='Breakers_branch_jur'),
    path('Breakers_substation_jur/<int:name_of_substation_id>/', breakers_substation_jur, name='Breakers_substation_jur'),
    path('jur_form/', add_commutation, name='jur_form'),



]
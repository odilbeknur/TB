from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('plants/', plants_view, name='plants'),
    path('commission/', commission_view, name='commission'),
    path('employer/', employer_view, name='employer'),
    path('create_employer/', employer_create, name='employer_create'),
    path('create_commission/', commission_create, name='commission_create')
]

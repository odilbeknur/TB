from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('plants/', plants_view, name='plants'),
    path('commission/', commission_view, name='commission'),
    path('employer/', employer_view, name='employer'),
    path('create_employer/', employer_create, name='employer_create'),
    path('create_commission/', commission_create, name='commission_create'),
    path('create_exam/', exam_create, name='exam_create'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('auth/', login_form, name='auth'),
    path('com_detail<int:pk>/', commission_detail, name='commission_detail'),
    path('emp_detail<int:pk>/', employer_detail, name='employer_detail'),
    path('plant_detail<int:pk>/', plants_detail, name='plant_detail'),
    path('exam/', exam_view, name='exam'),
    path('exam_detail<int:pk>/', exam_detail, name='exam_detail')
]

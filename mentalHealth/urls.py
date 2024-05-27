from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.mentalHealth,name = 'mentalhealth'),
    path('dashboard', views.dashboard, name='dashboard')
   
]

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.company_list, name='company'),
    path('company/<int:company_id>/', views.company_detail, name='company_detail'),
    path('add/', views.add_company, name="add") ,
    path('pitch', views.pitch, name='pitch'),
    path('create-message',views.create_message, name='create_message'),
]

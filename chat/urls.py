
from django.urls import path
from . import views

urlpatterns = [
  path('', views.chat_home, name='chat_home'),
    path('send/', views.send_message, name='send_message'),
    path('messages/', views.view_messages, name='view_messages'),
]
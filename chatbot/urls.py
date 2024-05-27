
from django.urls import path
from . import views

urlpatterns = [
    path('chatbot' , views.chat_view , name= 'chatbot'),
    path('image-captioning',views.image_captioning, name= 'imagebot')
    # path('', views.index, name='index'),
    # path('get-gemini-response/', views.get_gemini_response, name='get_gemini_response'),
]
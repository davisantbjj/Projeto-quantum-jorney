from django.urls import path
from . import views

urlpatterns = [
    path('whatsappbot/receive_message/', views.receive_message, name='receive_message'),
]

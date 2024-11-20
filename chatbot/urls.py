from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('whatsappbot.urls')),  # Certifique-se de que o 'nome_do_app' seja o nome correto do seu aplicativo
]

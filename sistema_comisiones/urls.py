# sistema_comisiones/urls.py
from django.contrib import admin
from django.urls import path, include # <-- Asegúrate de que 'include' esté importado

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('comisiones.urls')), # <-- Añade esta línea para la página principal
]
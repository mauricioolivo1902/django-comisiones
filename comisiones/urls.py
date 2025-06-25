# comisiones/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # La ruta vacía '' será la página principal de nuestra app
    path('', views.lista_ventas, name='lista_ventas'),
]
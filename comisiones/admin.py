# comisiones/admin.py

from django.contrib import admin
from .models import Vendedor, Venta, Regla

@admin.register(Vendedor)
class VendedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email')
    search_fields = ('nombre', 'apellido')

@admin.register(Regla)
class ReglaAdmin(admin.ModelAdmin):
    list_display = ('nombre_regla', 'porcentaje_comision')

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('vendedor', 'monto', 'fecha_venta', 'regla_aplicada', 'comision_calculada')
    list_filter = ('fecha_venta', 'vendedor', 'regla_aplicada')
    readonly_fields = ('comision_calculada',)
    date_hierarchy = 'fecha_venta'
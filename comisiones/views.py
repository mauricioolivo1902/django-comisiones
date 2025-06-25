# comisiones/views.py
from django.shortcuts import render
from .models import Venta
from .forms import FiltroFechaForm
from django.db.models import Sum # Para sumar los totales

def lista_ventas(request):
    form = FiltroFechaForm(request.GET or None)
    ventas = Venta.objects.select_related('vendedor', 'regla_aplicada').all()
    total_ventas = 0
    total_comisiones = 0

    if form.is_valid():
        fecha_inicio = form.cleaned_data.get('fecha_inicio')
        fecha_fin = form.cleaned_data.get('fecha_fin')

        if fecha_inicio and fecha_fin:
            ventas = ventas.filter(fecha_venta__range=[fecha_inicio, fecha_fin])

    # Calculamos los totales sobre el queryset filtrado (o completo si no hay filtro)
    if ventas:
        total_ventas = ventas.aggregate(Sum('monto'))['monto__sum'] or 0
        total_comisiones = ventas.aggregate(Sum('comision_calculada'))['comision_calculada__sum'] or 0


    context = {
        'form': form,
        'ventas': ventas.order_by('-fecha_venta'),
        'total_ventas': total_ventas,
        'total_comisiones': total_comisiones,
    }
    return render(request, 'comisiones/lista_ventas.html', context)
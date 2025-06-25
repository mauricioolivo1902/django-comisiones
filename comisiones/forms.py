# comisiones/forms.py
from django import forms

class FiltroFechaForm(forms.Form):
    fecha_inicio = forms.DateField(
        label='Fecha de inicio',
        widget=forms.DateInput(attrs={'type': 'date'}), # Esto crea un selector de fecha en el navegador
        required=False # Hacemos que los campos no sean obligatorios
    )
    fecha_fin = forms.DateField(
        label='Fecha de fin',
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False
    )
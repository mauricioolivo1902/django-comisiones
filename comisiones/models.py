# comisiones/models.py

from django.db import models

class Vendedor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Regla(models.Model):
    nombre_regla = models.CharField(max_length=100)
    porcentaje_comision = models.DecimalField(max_digits=5, decimal_places=2, help_text="Porcentaje de comisión, ej. 5.5 para 5.5%")
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre_regla} ({self.porcentaje_comision}%)"

class Venta(models.Model):
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE, related_name='ventas')
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_venta = models.DateField()
    regla_aplicada = models.ForeignKey(Regla, on_delete=models.SET_NULL, null=True, blank=True)
    comision_calculada = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, editable=False)

    def calcular_comision(self):
        if self.regla_aplicada:
            # Calculamos la comisión usando el monto y el porcentaje de la regla
            comision = self.monto * (self.regla_aplicada.porcentaje_comision / 100)
            return round(comision, 2)
        return 0

    def save(self, *args, **kwargs):
        # Antes de guardar la venta, calculamos su comisión
        self.comision_calculada = self.calcular_comision()
        super().save(*args, **kwargs) # Llamamos al método de guardado original

    def __str__(self):
        return f"Venta de {self.monto} por {self.vendedor.nombre} el {self.fecha_venta}"
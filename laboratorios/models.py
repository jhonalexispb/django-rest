from django.db import models

class LaboratorioModel(models.Model):
    nombre = models.CharField(max_length=100)
    margen_minimo = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=10)
    imagen = models.CharField(max_length = 255)
    imagen_portada = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'laboratorios'

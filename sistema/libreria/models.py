from django.db import models

class Auto(models.Model):
    id = models.AutoField(primary_key=True)
    Marca = models.CharField(max_length=50, verbose_name="Marca")
    Modelo = models.CharField(max_length=50, verbose_name="Modelo")
    Anio = models.CharField(max_length=4,verbose_name="Año")
    Placa = models.CharField(max_length=7,verbose_name="Placa")
    Disponibilidad = models.BooleanField(default=True)
    
    
    def __str__(self):
        fila = "Marca: " + self.Marca + " - " + "Modelo: " + self.Modelo
        return fila
    
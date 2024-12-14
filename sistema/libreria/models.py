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
    
    
class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    Nombres = models.CharField(max_length=100, verbose_name="Nombres")
    Apellidos= models.CharField(max_length=100, verbose_name="Apellidos")
    DNI= models.CharField(max_length=8, verbose_name="DNI")
    Email= models.EmailField(max_length=100, verbose_name="Email")
    Contrasena= models.CharField(max_length=30, verbose_name="Contraseña")
    Telefono= models.CharField(max_length=11, verbose_name="Teléfono")
    FechaNacimiento= models.DateField(verbose_name="Fecha de nacimiento")
    Direccion= models.CharField(max_length=100, verbose_name="Dirección")
    NroLicencia= models.CharField(max_length=10, verbose_name="Número de Licencia")
    FechaExpLicencia= models.DateField(verbose_name="Fecha de Expiración de Licencia")
    
    def __str__(self):
        fila = "Nombres: " + self.Nombres + " - " + "Apellido: " + self.Apellidos
        return fila

class Empleado(models.Model):
    id = models.AutoField(primary_key=True)
    User = models.CharField(max_length=100, verbose_name="User")
    Contrasena = models.CharField(max_length=30, verbose_name="Contraseña")
    NombresApellidos = models.CharField(max_length=100, verbose_name="Nombres y Apellidos")
    Cargo= models.CharField(max_length=30, verbose_name="Cargo")
    Email= models.CharField(max_length=100, verbose_name="Email")
    Telefono= models.CharField(max_length=11, verbose_name="Teléfono")
    
    def __str__(self):
        fila = "Cargo: " + self.Cargo + " - " + "Nombres: " + self.NombresApellidos
        return fila



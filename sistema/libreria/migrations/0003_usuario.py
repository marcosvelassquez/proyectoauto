# Generated by Django 5.1.4 on 2024-12-12 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0002_remove_auto_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Nombres', models.CharField(max_length=100, verbose_name='Nombres')),
                ('Apellidos', models.CharField(max_length=100, verbose_name='Apellidos')),
                ('DNI', models.CharField(max_length=8, verbose_name='DNI')),
                ('Email', models.CharField(max_length=100, verbose_name='Email')),
                ('Contrasena', models.CharField(max_length=30, verbose_name='Contraseña')),
                ('Telefono', models.CharField(max_length=11, verbose_name='Teléfono')),
                ('FechaNacimiento', models.DateField(verbose_name='Fecha de nacimiento')),
                ('Direccion', models.CharField(max_length=100, verbose_name='Dirección')),
                ('NroLicencia', models.CharField(max_length=10, verbose_name='Número de Licencia')),
                ('FechaExpLicencia', models.DateField(verbose_name='DNI')),
            ],
        ),
    ]

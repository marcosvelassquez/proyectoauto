# Generated by Django 5.1.4 on 2024-12-13 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0003_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('User', models.CharField(max_length=100, verbose_name='User')),
                ('Contrasena', models.CharField(max_length=30, verbose_name='Contraseña')),
                ('NombresApellidos', models.CharField(max_length=100, verbose_name='Nombres y Apellidos')),
                ('Cargo', models.CharField(max_length=30, verbose_name='Cargo')),
                ('Email', models.CharField(max_length=100, verbose_name='Email')),
                ('Telefono', models.CharField(max_length=11, verbose_name='Teléfono')),
            ],
        ),
        migrations.AlterField(
            model_name='usuario',
            name='FechaExpLicencia',
            field=models.DateField(verbose_name='Fecha de Expiración de Licencia'),
        ),
    ]

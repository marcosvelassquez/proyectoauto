from django.urls import path
from . import views

urlpatterns = [
    path('', views.usuarios, name='usuarios'),
    path('empleados', views.empleados, name='empleados'),
    path('autos', views.autos, name='autos'),
    path('autos/crear', views.crear_auto, name='crear_auto'),
    path('autos/editar', views.editar_auto, name='editar_auto'),
    path('eliminar/<int:id>', views.eliminar_auto, name='eliminar_auto'),
    path('autos/editar/<int:id>', views.editar_auto, name='editar_auto'),
]


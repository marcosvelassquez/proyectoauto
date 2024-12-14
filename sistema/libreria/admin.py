from django.contrib import admin
from.models import Auto
from.models import Usuario


admin.site.register(Auto)
admin.site.register(Usuario)


# Register your models here.

#python manage.py createsuperuser
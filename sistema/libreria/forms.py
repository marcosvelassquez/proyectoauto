from django import forms
from .models import Auto
from.models import Usuario
from.models import Empleado


class AutoForm(forms.ModelForm):
    class Meta:
        model = Auto
        fields = '__all__'
        
class UsuarioForm(forms.ModelForm):
    # contrasena = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Usuario
        fields = '__all__'
        
class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'
        
        

    
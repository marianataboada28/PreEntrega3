from django import forms
from .models import Curso

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'descripcion']

class BusquedaForm(forms.Form):
    busqueda = forms.CharField(max_length=100)

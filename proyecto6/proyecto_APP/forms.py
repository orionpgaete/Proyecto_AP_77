from dataclasses import fields
from django import forms
from proyecto_APP.models import Proyecto

class FormProyecto(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = '__all__'
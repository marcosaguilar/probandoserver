from django import forms
from models import recurso


class CrearRecursoForm(forms.ModelForm):
    """este formulario permite cargar los datos de recurso"""

    class Meta:
        model = recurso

        fields = [
            'nombre',
            #'estado',
            #'mantenimiento',
            'tipo',
        ]
        labels = {
            'nombre': 'Nombre del recurso o identificador',
            #'estado': 'Estado de disponibilidad',
            #'mantenimiento': 'Tipo de mantenimiento',
            'tipo': 'Tipo de recurso',
        }
        widgets = {
            'nombre': forms.TextInput(),
            #'estado': forms.Select(),
            #'mantenimiento': forms.Select(),
            'tipo': forms.Select(),
        }

class EditarRecursoForm(forms.ModelForm):
    """este formulario permite cargar los datos de recurso"""
    class Meta:
        model = recurso

        fields = [
            'nombre',
            'estado',
            #'mantenimiento',
            'tipo',
        ]
        labels = {
            'nombre': 'Nombre del recurso o identificador',
            'estado': 'Estado de disponibilidad',
            #'mantenimiento': 'Tipo de mantenimiento',
            'tipo': 'Tipo de recurso',
        }
        widgets = {
            'nombre': forms.TextInput(),
            'estado': forms.Select(),
            #'mantenimiento': forms.Select(),
            'tipo': forms.Select(),
        }


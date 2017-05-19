from django import forms
from models import recurso, Tipo_de_recurso


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

class CrearTipoRecursoForm(forms.ModelForm):
    """este formulario permite cargar los datos de un tipo de recurso para su creacion"""
    class Meta:
        model = Tipo_de_recurso

        fields = [
            'nombre',
            'descripcion',
        ]
        labels = {
            'nombre': 'Nombre del tipo de recurso',

            'descripcion': 'describa el tipo de recurso',
        }
        widgets = {
            'nombre': forms.TextInput(),
            'descripcion': forms.TextInput(),
        }

from django import forms
<<<<<<< HEAD
from models import recurso, Tipo_de_recurso
=======
from models import recurso, Mantenimiento
>>>>>>> developerMA


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

<<<<<<< HEAD
class CrearTipoRecursoForm(forms.ModelForm):
    """este formulario permite cargar los datos de un tipo de recurso para su creacion"""
    class Meta:
        model = Tipo_de_recurso
=======

class CrearMantenimientoForm(forms.ModelForm):
    """este formulario permite cargar los datos del mantenimiento"""

    class Meta:
        model = Mantenimiento
>>>>>>> developerMA

        fields = [
            'nombre',
            'descripcion',
<<<<<<< HEAD
        ]
        labels = {
            'nombre': 'Nombre del tipo de recurso',

            'descripcion': 'describa el tipo de recurso',
=======
            'fechainicio',
            'fechafin',
        ]
        labels = {
            'nombre': 'Nombre del mantenimiento',
            'descripcion': 'Descripcion del mantenimiento',
            'fechainicio': 'Fecha de inicio',
            'fechafin': 'Fecha de termino',
>>>>>>> developerMA
        }
        widgets = {
            'nombre': forms.TextInput(),
            'descripcion': forms.TextInput(),
<<<<<<< HEAD
        }
=======
            'fechainicio': forms.TextInput(),
            'fechafin': forms.TextInput(),
        }
>>>>>>> developerMA

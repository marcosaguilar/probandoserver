from django import forms
<<<<<<< HEAD
from models import recurso, Tipo_de_recurso, Mantenimiento
=======

from models import recurso, Tipo_de_recurso, Mantenimiento

>>>>>>> 5f4e0dce1050b8d0da6ae6523ecda450357b4c4e


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
            'mantenimiento',
            'tipo',
        ]
        labels = {
            'nombre': 'Nombre del recurso o identificador',
            'estado': 'Estado de disponibilidad',
            'mantenimiento': 'Tipo de mantenimiento',
            'tipo': 'Tipo de recurso',
        }
        widgets = {
            'nombre': forms.TextInput(),
            'estado': forms.Select(),
            'mantenimiento': forms.Select(),
            'tipo': forms.Select(),
        }

<<<<<<< HEAD
=======
class CrearMantenimientoForm(forms.ModelForm):
    """este formulario permite cargar los datos de mantenimiento"""
    class Meta:
        model = Mantenimiento

        fields = [
            'estado',
            'tipo',
            'descripcion',
            'fecha_inicio',
            'fecha_fin',
            'cod_recurso',
        ]
        labels = {

            'estado': 'Estado del recurso en mantenimiento',
            'tipo': 'Tipo de mantenimiento',
            'descripcion': 'Descripcion del problema del recurso',
            'fecha_inicio': 'fecha de inicio del mantenimiento',
            'fecha_fin': 'fecha estimada del fin del mantenimiento',
            'cod_recurso':'codigo del recurso',
        }
        widgets = {
            'nombre': forms.TextInput(),
            'estado': forms.TextInput(),
            'tipo': forms.Select(),
            'descripcion': forms.TextInput(),
            'fecha_inicio': forms.TextInput(),
            'fecha_fin': forms.TextInput(),
            'recurso_id': forms.HiddenInput(),
        }

>>>>>>> 5f4e0dce1050b8d0da6ae6523ecda450357b4c4e

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

<<<<<<< HEAD

class CrearMantenimientoForm(forms.ModelForm):
    """este formulario permite cargar los datos del mantenimiento"""

    class Meta:
        model = Mantenimiento

        fields = [
            'nombre',
            'descripcion',
            'fechainicio',
            'fechafin',
        ]
        labels = {
            'nombre': 'Nombre del mantenimiento',
            'descripcion': 'Descripcion del mantenimiento',
            'fechainicio': 'Fecha de inicio',
            'fechafin': 'Fecha de termino',
        }
        widgets = {
            'nombre': forms.TextInput(),
            'descripcion': forms.TextInput(),
            'fechainicio': forms.TextInput(),
            'fechafin': forms.TextInput(),
        }
=======
>>>>>>> 5f4e0dce1050b8d0da6ae6523ecda450357b4c4e

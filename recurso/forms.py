from django import forms
from models import recurso, Tipo_de_recurso, Mantenimiento


class RecursoSinTipoReporteForm(forms.ModelForm):
    """este formulario permite cargar obtener un dato para filtrado de un recurso"""

    class Meta:
        model = recurso

        fields = [
            'estado',


        ]
        labels = {
            'estado': 'Estado del recurso',

        }
        widgets = {
            'estado': forms.Select(),

        }


class RecursoReporteForm(forms.ModelForm):
    """este formulario permite cargar los datos de filtrado de  recurso"""

    class Meta:
        model = recurso

        fields = [
            'estado',
            'tipo',

        ]
        labels = {
            'estado': 'Estado del recurso',
            'tipo': 'Tipo de recurso',
        }
        widgets = {
            'estado': forms.Select(),
            'tipo': forms.Select(),
        }







class CrearRecursoForm(forms.ModelForm):
    """este formulario permite cargar los datos de recurso"""

    class Meta:
        model = recurso

        fields = [
            'nombre',
            'tipo',
        ]
        labels = {
            'nombre': 'Nombre del recurso o identificador',
            'tipo': 'Tipo de recurso',
        }
        widgets = {
            'nombre': forms.TextInput(),
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
            'mantenimiento': 'Mantenimiento',
            'tipo': 'Tipo de recurso',
        }
        widgets = {
            'nombre': forms.TextInput(),
            'estado': forms.Select(),
            'mantenimiento': forms.Select(),
            'tipo': forms.Select(),
        }



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
            'estado': forms.Select(),
            'tipo': forms.Select(),
            'descripcion': forms.TextInput(),
            'fecha_inicio': forms.TextInput(),
            'fecha_fin': forms.TextInput(),
            'recurso_id': forms.HiddenInput(),
        }


class EditarMantenimientoForm(forms.ModelForm):
    """este formulario permite cargar los datos de mantenimiento"""
    class Meta:
        model = Mantenimiento

        fields = [
            'estado',
            'tipo',
            'descripcion',
            'fecha_inicio',
            'fecha_fin',
            #'cod_recurso',
        ]
        labels = {

            'estado': 'Estado del recurso en mantenimiento',
            'tipo': 'Tipo de mantenimiento',
            'descripcion': 'Descripcion del problema del recurso',
            'fecha_inicio': 'fecha de inicio del mantenimiento',
            'fecha_fin': 'fecha estimada del fin del mantenimiento',
            #'cod_recurso':'codigo del recurso',
        }
        widgets = {
            'nombre': forms.TextInput(),
            'estado': forms.Select(),
            'tipo': forms.Select(),
            'descripcion': forms.TextInput(),
            'fecha_inicio': forms.TextInput(),
            'fecha_fin': forms.TextInput(),

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


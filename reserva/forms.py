from django import forms
from models import reserva

# Create your forms here.

class CrearReservaForm(forms.ModelForm):
    """este form permite crear una reserva con los campos correspondientes"""
    class Meta:
        model = reserva

        fields = [
            'recurso',
            #'tipo_recurso',
            #'usuario',
            'fecha_inicio',
            'fecha_fin',
            #'estado_reserva',
        ]
        labels = {
            'recurso': 'Recurso reservado',
            #'tipo_recurso': 'Tipo del recurso reservado',
            #'usuario': 'Usuario que realiza la reserva',
            'fecha_inicio': 'Fecha inicio',
            'fecha_fin': 'Fecha fin',
            #'estado_reserva': 'Estado de la reserva',
        }
        widgets = {
            'recurso': forms.Select(),
            #'tipo_recurso': forms.Select(),
            #'usuario': forms.Select(),
            'fecha_inicio': forms.TextInput(),
            'fecha_fin': forms.TextInput(),
            #'estado_reserva': forms.Select(),
        }


class EditarReservaForm(forms.ModelForm):
    """este form permite editar una reserva con los campos correspondientes"""
    class Meta:
        model = reserva

        fields = [
            'recurso',
            #'tipo_recurso',
            #'usuario',
            'fecha_inicio',
            'fecha_fin',
            'estado_reserva',
            'gano_reserva',
        ]
        labels = {
            'recurso': 'Recurso reservado',
            #'tipo_recurso': 'Tipo del recurso reservado',
            #'usuario': 'Usuario que realiza la reserva',
            'fecha_inicio': 'Fecha inicio',
            'fecha_fin': 'Fecha fin',
            'estado_reserva': 'Estado de la reserva',
            'gano_reserva': 'Estado de reserva'
        }
        widgets = {
            'recurso': forms.Select(),
            #'tipo_recurso': forms.Select(),
            #'usuario': forms.Select(),
            'fecha_inicio': forms.TextInput(),
            'fecha_fin': forms.TextInput(),
            'estado_reserva': forms.Select(),
            'gano_reserva': forms.NumberInput(),
        }
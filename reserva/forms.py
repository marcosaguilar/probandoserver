from django import forms
from models import reserva

# Create your forms here.

class ReservaReporteForm(forms.ModelForm):
    """este form permite filtrar una reserva con los campos correspondientes"""
    class Meta:
        model = reserva
        #exclude = ('fecha_inicio','fecha_fin','estado_reserva')

        #def clean_tipo_reserva(self):
        #    tipo_reserva = self.clean_tipo_reserva['tipo_reserva']
        #    return tipo_reserva

        fields = [
            #'recurso',
            #'tipo_recurso',
            'tipo_reserva',
            #'usuario',
            'fecha_inicio',
            'fecha_fin',
            'estado_reserva',
        ]
        labels = {
            #'recurso': 'Recurso reservado',
            #'tipo_recurso': 'Tipo del recurso reservado',
            'tipo_reserva':'Tipo de reserva ',
            #'usuario': 'Usuario que realiza la reserva',
            'fecha_inicio': 'Fecha inicio',
            'fecha_fin': 'Fecha fin',
            'estado_reserva': 'Estado de la reserva',
        }
        widgets = {
            #'recurso': forms.Select(),
            #'tipo_recurso': forms.Select(),
            'tipo_reserva': forms.TextInput(),
            #'usuario': forms.Select(),
            'fecha_inicio': forms.TextInput(),
            'fecha_fin': forms.TextInput(),
            'estado_reserva': forms.Select(),
        }





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



class CrearReservaGeneralForm(forms.ModelForm):
    """este form permite crear una reserva con los campos correspondientes"""
    class Meta:
        model = reserva

        fields = [
            #'recurso',
            'tipo_recurso',
            #'usuario',
            'fecha_inicio',
            'fecha_fin',
            #'estado_reserva',
        ]
        labels = {
            #'recurso': 'Recurso reservado',
            'tipo_recurso': 'Tipo del recurso reservado',
            #'usuario': 'Usuario que realiza la reserva',
            'fecha_inicio': 'Fecha inicio',
            'fecha_fin': 'Fecha fin',
            #'estado_reserva': 'Estado de la reserva',
        }
        widgets = {
            #'recurso': forms.Select(),
            'tipo_recurso': forms.Select(),
            #'usuario': forms.Select(),
            'fecha_inicio': forms.TextInput(),
            'fecha_fin': forms.TextInput(),
            #'estado_reserva': forms.Select(),
        }


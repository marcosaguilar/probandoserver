from django import forms
from django.contrib.auth.models import Group
from models import usuario, rol


class UsuarioForm(forms.ModelForm):
    """este formulario permite crear un usuario con los campos correspondientes"""
    class Meta:
        model = usuario

        fields = [
            'username',
            'password',
            'cedula',
            'nombres',
            'apellidos',
            'email',
            'telefono',
            'direccion',
            'rol',
            #'prioridad',
        ]
        labels = {
            'username': 'Nombre de usuario',
            'password': 'Contrasena',
            'cedula': 'Cedula',
            'nombres': 'Nombres',
            'apellidos': 'Apellidos',
            'email': 'Email',
            'telefono': 'Telefono',
            'direccion': 'Direccion',
            'rol': 'Roles',
            #'prioridad': 'Prioridad Para Reserva',
        }
        widgets = {
            'username': forms.TextInput(),
            'password': forms.PasswordInput(),
            'cedula': forms.NumberInput(),
            'nombres': forms.TextInput(),
            'apellidos': forms.TextInput(),
            'email': forms.EmailInput(),
            'telefono': forms.TextInput(),
            'direccion': forms.TextInput(),
            'rol': forms.CheckboxSelectMultiple(),
            #'prioridad': forms.Select()
        }

class EditarUsuarioForm(forms.ModelForm):
    """este form permite editar ciertos datos de un usuario"""
    class Meta:
        model = usuario

        fields = [
            'username',
            'password',
            'cedula',
            'nombres',
            'apellidos',
            'email',
            'telefono',
            'direccion',
            'rol',
        ]
        labels = {
            'username': 'Nombre de usuario',
            'password': 'Contrasena',
            'cedula': 'Cedula',
            'nombres': 'Nombres',
            'apellidos': 'Apellidos',
            'email': 'Email',
            'telefono': 'Telefono',
            'direccion': 'Direccion',
            'rol': 'Roles',
            #'prioridad': 'Prioridad Para Reserva',
        }
        widgets = {
            'username': forms.TextInput(),
            'password': forms.PasswordInput(),
            'cedula': forms.NumberInput(),
            'nombres': forms.TextInput(),
            'apellidos': forms.TextInput(),
            'email': forms.EmailInput(),
            'telefono': forms.TextInput(),
            'direccion': forms.TextInput(),
            'rol': forms.CheckboxSelectMultiple(),
            #'prioridad': forms.Select()
        }

class CrearRolForm(forms.ModelForm):
    """este form permite crear un rol con los campos correspondientes"""
    class Meta:
        model = rol

        fields = [
            'nombre',
            'permisos',
            'prioridad',
            #'tipoRecurso',
        ]
        labels = {
            'nombre': 'Nombre del rol',
            'permisos': 'Permisos',
            'prioridad': 'Prioridad Para Reserva',
            #'tipoRecurso':'Tipo de recurso',
        }
        widgets = {
            'nombre': forms.TextInput(),
            'permisos': forms.CheckboxSelectMultiple(),
            'prioridad': forms.Select()
            #'tipoRecurso': forms.Select(),
        }


class EditarRolForm(forms.ModelForm):
    """este form permite editar ciertos campos de un rol"""
    class Meta:
        model = rol

        fields = [
            'nombre',
            'permisos',
            'tipoRecurso',
            'prioridad',
        ]
        labels = {
            'nombre': 'Nombre del rol',
            'permisos': 'Permisos',
            'tipoRecurso':'Tipo de recurso',
            'prioridad': 'Prioridad Para Reserva',
        }
        widgets = {
            'nombre': forms.TextInput(),
            'permisos': forms.CheckboxSelectMultiple(),
            'tipoRecurso': forms.Select(),
            'prioridad': forms.Select(),
        }

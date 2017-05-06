from django import forms
from django.contrib.auth.models import Group
from models import usuario, rol


class UsuarioForm(forms.ModelForm):

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
        }

class EditarUsuarioForm(forms.ModelForm):

    class Meta:
        model = usuario

        fields = [

            'cedula',
            'nombres',
            'apellidos',
            'email',
            'telefono',
            'direccion',
            'groups',
        ]
        labels = {

            'cedula': 'Cedula',
            'nombres': 'Nombres',
            'apellidos': 'Apellidos',
            'email': 'Email',
            'telefono': 'Telefono',
            'direccion': 'Direccion',
            'groups': 'Roles',
        }
        widgets = {

            'cedula': forms.NumberInput(),
            'nombres': forms.TextInput(),
            'apellidos': forms.TextInput(),
            'email': forms.EmailInput(),
            'telefono': forms.TextInput(),
            'direccion': forms.TextInput(),
            'groups': forms.CheckboxSelectMultiple(),
        }

class CrearRolForm(forms.ModelForm):

    class Meta:
        model = rol

        fields = [
            'nombre',
            'permisos',
            #'tipoRecurso',
        ]
        labels = {
            'nombre': 'Nombre del rol',
            'permisos': 'Permisos',
            #'tipoRecurso':'Tipo de recurso',
        }
        widgets = {
            'nombre': forms.TextInput(),
            'permisos': forms.CheckboxSelectMultiple(),
            #'tipoRecurso': forms.Select(),
        }


class ModificarRolForm(forms.ModelForm):

    class Meta:
        model = rol

        fields = [
            'nombre',
            'permisos',
            'tipoRecurso',
        ]
        labels = {
            'nombre': 'Nombre del rol',
            'permisos': 'Permisos',
            'tipoRecurso':'Tipo de recurso',
        }
        widgets = {
            'nombre': forms.TextInput(),
            'permisos': forms.CheckboxSelectMultiple(),
            'tipoRecurso': forms.Select(),
        }

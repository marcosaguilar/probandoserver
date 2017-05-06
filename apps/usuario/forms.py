from django import forms
from django.contrib.auth.models import Group
from models import usuario


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
            'groups',
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
            'groups': 'Roles',
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
            'groups': forms.CheckboxSelectMultiple(),
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
        model = Group

        fields = [
            'name',
            'permissions',
        ]
        labels = {
            'name': 'Nombre del rol',
            'permissions': 'Permisos',
        }
        widgets = {
            'name': forms.TextInput(),
            'permissions': forms.CheckboxSelectMultiple(),
        }

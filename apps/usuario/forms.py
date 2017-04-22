from django import forms

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
            'rol': 'Rol',
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



class CrearRolForm(forms.ModelForm):

    class Meta:
        model = rol

        fields = [
            'nombre',
            'descripcion',
            'permisos',
        ]
        labels = {
            'nombre': 'Nombre del rol',
            'descripcion': 'Descripcion',
            'permisos': 'Permisos',
        }
        widgets = {
            'nombre': forms.TextInput(),
            'descripcion': forms.TextInput(),
            'permisos': forms.CheckboxSelectMultiple(),
        }

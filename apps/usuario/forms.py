from django import forms

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
        ]
        labels = {
            'username' : 'Nombre de usuario',
            'password' : 'Contrasena',
            'cedula': 'Cedula',
            'nombres' : 'Nombres',
            'apellidos' : 'Apellidos',
            'email' : 'Email',
            'telefono' : 'Telefono',
            'direccion' : 'Direccion',
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
        }
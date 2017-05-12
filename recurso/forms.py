from django import forms
from models import recurso


class CrearRecursoForm(forms.ModelForm):
    """este formulario permite cargar los datos de recurso"""
    #def __init__(self, *args, **kwargs):
    #    self.listaderoles = []
    #    super(CrearRecursoForm, self).__init__(*args, **kwargs)

    #def pasarRol(self, request):
        #listaderoles = []
    #    for roles in request.user.rol.all():
    #        self.listaderoles.append(roles)
    #    self.fields['tipo'].queryset = tipo.objects.filter(supplier = self.listaderoles)
    #    print (self.listaderoles)

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


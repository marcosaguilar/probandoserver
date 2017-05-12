from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required, login_required
from forms import CrearRecursoForm, EditarRecursoForm
from models import Tipo_de_recurso
# Create your views here.

from models import EstadoRecurso,recurso#, Mantenimiento


def index(request):
    return render(request, 'usuario/index.html')



@permission_required('recurso.add_recurso')
def crearRecurso_view(request):
    """crea un recurso en el sistema"""
    if request.method == 'POST':
        form = CrearRecursoForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.estado = EstadoRecurso.objects.get(estado='Disponible')
            #form.mantenimiento = Mantenimiento.objects.get(estado='Sin tipo')
            form.save()
            return redirect('login_page')
        return redirect('recurso:listar_recurso')
    else:
        form = CrearRecursoForm()
        listadetipos = []
        for roles in request.user.rol.all():
            listadetipos.append(roles.tipoRecurso.nombre)

        form.fields["tipo"].queryset = Tipo_de_recurso.objects.filter(nombre__in = listadetipos)

    return render(request,'recurso/crearRecurso_form.html', {'form': form})


@permission_required('recurso.ver_recurso')
def listarRecurso_view(request):
    """despliega la lista de recursos registrados en el sistema de los tipos de recurso que el usuario administra"""
    lista = []
    for roldelusuario in request.user.rol.all():
        tiporecursodelusuario = roldelusuario.tipoRecurso
        nuevalista = recurso.objects.filter(tipo=tiporecursodelusuario).order_by('id')
        for elemento in nuevalista:
            lista.append(elemento)

    contexto = {'recursos': lista}
    return render(request,'recurso/listar_recurso.html', contexto)


@permission_required('recurso.change_recurso')
def editarRecurso_view(request, id_recurso):
    """permite modificar los atributos de un recurso"""
    var_recurso = recurso.objects.get(id=id_recurso)
    if request.method == 'GET':
        form = EditarRecursoForm(instance=var_recurso)
    else:
        form = EditarRecursoForm(request.POST, instance=var_recurso)
        if form.is_valid():
            form.save()
        return redirect('recurso:listar_recurso')
    return render(request, 'recurso/crearRecurso_form.html', {'form': form})


@permission_required('recurso.delete_recurso')
def eliminarRecurso_view(request, id_recurso):
    """borra un Recurso registrado de la base de datos del sistema"""
    var_recurso = recurso.objects.get(id=id_recurso)
    if request.method == 'POST':
        var_recurso.delete()
        return redirect('recurso:listar_recurso')
    return render(request,'recurso/eliminar_recurso.html', {'recurso_aux': var_recurso})
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required, login_required
from forms import CrearRecursoForm, EditarRecursoForm, CrearMantenimientoForm
# Create your views here.

from models import EstadoRecurso,recurso, Mantenimiento


def index(request):
    return render(request, 'usuario/index.html')



#@permission_required('recurso.add_recurso')
def crearRecurso_view(request):
    """crea un recurso en el sistema"""
    if request.method == 'POST':
        form = CrearRecursoForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.estado = EstadoRecurso.objects.get(estado='Disponible')
            form.save()
            return redirect('login_page')
        return redirect('recurso:listar_recurso')
    else:
        form = CrearRecursoForm()

    return render(request,'recurso/crearRecurso_form.html', {'form': form})


#@permission_required('recurso.ver_recurso')
def listarRecurso_view(request):
    """despliega una lista de recursos registrados en el sistema"""
    lista = recurso.objects.all().order_by('id')
    contexto = {'recursos':lista}
    return render(request,'recurso/listar_recurso.html', contexto)


#@permission_required('recurso.change_recurso')
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


#@permission_required('recurso.delete_recurso')
def eliminarRecurso_view(request, id_recurso):
    """borra un Recurso registrado de la base de datos del sistema"""
    var_recurso = recurso.objects.get(id=id_recurso)
    if request.method == 'POST':
        var_recurso.delete()
        return redirect('recurso:listar_recurso')
    return render(request,'recurso/eliminar_recurso.html', {'recurso_aux': var_recurso})



def crearMantenimiento_view(request, id_recurso):
    if request.method == 'POST':
        form = CrearMantenimientoForm(request.POST)
        if form.is_valid():
            man = form.save(commit=False)
            man.estado = "A realizar"
            man.cod_recurso = id_recurso
            man.save()
            var_recurso = recurso.objects.get(id=id_recurso)
            form1 = EditarRecursoForm(instance=var_recurso)
            rec = form1.save(commit=False)
            rec.mantenimiento = Mantenimiento.objects.get(cod_recurso=id_recurso)
            rec.save()
            return redirect('recurso:listar_rec_man')

        return redirect('recurso:listar_recurso')
    else:
        form = CrearMantenimientoForm()

    return render(request,'recurso/crearMantenimiento_form.html', {'form': form})

def listarMantenimiento_view(request):
    lista = recurso.objects.all().order_by('id')
    contexto = {'recursos':lista}
    return render(request,'recurso/listar_rec_man.html', contexto)

def listarAsignarMantenimiento_view(request):
    lista = recurso.objects.all().order_by('id')
    contexto = {'recursos': lista}
    return render(request, 'recurso/listar_asignar_man.html', contexto)
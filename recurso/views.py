from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required, login_required
from forms import CrearRecursoForm
# Create your views here.

from models import EstadoRecurso,recurso#, Mantenimiento


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
            #form.mantenimiento = Mantenimiento.objects.get(estado='Sin tipo')
            form.save()
            return redirect('login_page')
        return redirect('recurso:listar_recurso')
    else:
        form = CrearRecursoForm()

    return render(request,'recurso/crearRecurso_form.html', {'form': form})

def listarRecurso_view(request):
    """despliega una lista de recursos registrados en el sistema"""
    lista = recurso.objects.all().order_by('id')
    contexto = {'recursos':lista}
    return render(request,'recurso/listar_recurso.html', contexto)

def eliminarRecurso_view(request, id_recurso):
    """borra un Recurso registrado de la base de datos del sistema"""
    var_recurso = recurso.objects.get(id=id_recurso)
    if request.method == 'POST':
        var_recurso.delete()
        return redirect('recurso:listar_recurso')
    return render(request,'recurso/eliminar_recurso.html', {'recurso_aux': var_recurso})
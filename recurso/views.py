from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from models import EstadoRecurso,recurso, Mantenimiento ,Tipo_de_recurso
from forms import CrearRecursoForm, EditarRecursoForm, CrearTipoRecursoForm, EditarMantenimientoForm, CrearMantenimientoForm

# Create your views here.


def index(request):
    return render(request, 'usuario/index.html')


@permission_required('recurso.add_recurso', login_url='/login/')
def crearRecurso_view(request):
    """crea un recurso en el sistema"""
    if request.method == 'POST':
        form = CrearRecursoForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.estado = EstadoRecurso.objects.get(estado='Disponible')
            #form.estado = EstadoRecurso.objects.get(estado='Disponible')
            #form.mantenimiento = Mantenimiento.objects.get(estado='Sin tipo')

            form.save()
            return redirect('login_page')
        return redirect('recurso:listar_recurso')
    else:
        form = CrearRecursoForm()
        #filtrar solo los tipo de recurso que administra el usuario
        listadetipos = []
        for roles in request.user.rol.all():
            if roles.tipoRecurso: #si es un rol con tipo de recurso, es decir un administrador de recursos
                listadetipos.append(roles.tipoRecurso.nombre)
        form.fields["tipo"].queryset = Tipo_de_recurso.objects.filter(nombre__in=listadetipos)

    return render(request,'recurso/crearRecurso_form.html', {'form': form})


@permission_required('recurso.ver_recurso', login_url='/login/')
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


@permission_required('recurso.change_recurso', login_url='/login/')
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


@permission_required('recurso.delete_recurso', login_url='/login/')
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


def editarMantenimiento_view(request, id_mantenimiento):
    """permite modificar los atributos de un mantenimiento"""
    var = Mantenimiento.objects.get(id=id_mantenimiento)
    if request.method == 'GET':
        form = EditarMantenimientoForm(instance=var)
        #aux = form.save(commit=False)
    else:
        form = EditarMantenimientoForm(request.POST, instance=var)
        #man = form.save(commit=False)
        if form.is_valid():
            form.save()
            return redirect('recurso:listar_mantenimiento')
    return render(request, 'recurso/editar_mantenimiento.html', {'form': form})


def listarMantenimiento_view(request):
    lista = Mantenimiento.objects.all().order_by('id')
    contexto = {'mantenimientos': lista}
    return render(request, 'recurso/listar_mantenimiento.html', contexto)

def listarRecursoMantenimiento_view(request):
    lista = recurso.objects.all().order_by('id')
    contexto = {'recursos':lista}
    return render(request,'recurso/listar_rec_man.html', contexto)

def listarAsignarMantenimiento_view(request):
    lista = recurso.objects.all().order_by('id')
    contexto = {'recursos': lista}
    return render(request, 'recurso/listar_asignar_man.html', contexto)


@permission_required('recurso.add_tipo_de_recurso', login_url='/login/')
def crearTipo_Recurso_view(request):
    """crea un tipo de recurso en el sistema"""
    if request.method == 'POST':
        form = CrearTipoRecursoForm(request.POST)
        if form.is_valid():
            #form = form.save(commit=False)

            form.save()
            return redirect('home_page')
        return redirect('login_page')
    else:
        form = CrearTipoRecursoForm()

    return render(request,'recurso/crearTipoRecurso_form.html', {'form': form})


@permission_required('recurso.ver_tipo_de_recurso', login_url='/login/')
def listarTipoRecurso_view(request):
    """despliega una lista de tipos de recurso registrados en el sistema"""
    lista1 = Tipo_de_recurso.objects.all().order_by('id')
    contexto1 = {'tipos':lista1}
    return render(request,'recurso/listar_tiporecurso.html', contexto1)


@permission_required('recurso.delete_tipo_de_recurso', login_url='/login/')
def eliminarTipoRecurso_view(request, id_Tipo_de_recurso):
    """borra un Tipo de Recurso registrado de la base de datos del sistema"""
    var_Tipo_de_recurso = Tipo_de_recurso.objects.get(id=id_Tipo_de_recurso)
    if request.method == 'POST':
        var_Tipo_de_recurso.delete()
        return redirect('recurso:listar_tiporecurso')
    return render(request,'recurso/eliminar_tiporecurso.html', {'Tipo_de_recurso_aux': var_Tipo_de_recurso})



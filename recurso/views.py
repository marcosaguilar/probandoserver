from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from models import EstadoRecurso,recurso, Mantenimiento ,Tipo_de_recurso, estadoMantenimiento
from forms import CrearRecursoForm, EditarRecursoForm, CrearTipoRecursoForm, EditarMantenimientoForm, CrearMantenimientoForm
from datetime import datetime

# Create your views here.



#--------------------------------------------Reportes-----------------------------------
#--------------------------------------------------------------------------------------

from forms import RecursoReporteForm, RecursoSinTipoReporteForm
from probandoserver.views import render_to_pdf
from usuario.models import rol, usuario



from django.http import HttpResponse

def reporte_listaroles(request):
    """genera una lista de los roles que administran los recursos del sistema"""

    lista = rol.objects.exclude(tipoRecurso=None)
    contexto = {'roles': lista}
    return render(request, 'recurso/reporteRoles.html', contexto)


def reporte_conrol(request, id_rol):
    """ genera una lista de usuarios que tienen el rol seleccionado"""
    lista = []
    listarol = []
    listarol.append(id_rol)
    if id_rol:
        asignado =rol.objects.get(id=id_rol)
        for usuarios in usuario.objects.all():
            for roles in usuarios.rol.all():
                if roles.id == asignado.id:
                    lista.append(usuarios)

    return render(request, 'recurso/reporteUsuarios.html', {'usuarios': lista, 'rol':listarol})

class datos:
    id = ""
    nombre = ""
    tipo = ""
    estado = ""
    responsable = ""
    def __init__(self, a, b,c,d,e):
        self.id = a
        self.nombre = b
        self.tipo = c
        self.estado = d
        self.responsable = e


def crear_reporteconuser(request,id_usuario,id_rol):
    """ genera los datos para el reporte considerando un responsable el recurso en el filtrado"""
    lista1 =[]
    lista2 = []
    if request.method == 'POST':
        form = RecursoSinTipoReporteForm(request.POST)
        if form.is_valid():
            aux = form.save(commit=False)
            varrol = rol.objects.get(id=id_rol)


            if aux.estado:
                lista1 = recurso.objects.filter(tipo=varrol.tipoRecurso,estado=aux.estado).order_by('id')
            else:
                lista1 = recurso.objects.filter(tipo=varrol.tipoRecurso)

            listafinal = []

            usuarios = usuario.objects.get(id=id_usuario)
            for recursos in lista1:
                aux = datos(recursos.id,recursos.nombre,recursos.tipo,recursos.estado,usuarios.nombres)
                listafinal.append(aux)

            context = {'recursos': listafinal}
            pdf = render_to_pdf('recurso/reporteRecurso.html', context)
            if pdf:
                return HttpResponse(pdf, content_type='application/pdf')
            return HttpResponse("No se encontraron los datos")

        return HttpResponse("Formulario no valido")

    else:
        form = RecursoSinTipoReporteForm()
    return render(request, 'recurso/crearReporteRecurso.html', {'form': form})


def crear_reportesinuser(request):
    """ genera los datos para el reporte considerando el estado y tipo de recurso"""

    if request.method == 'POST':
        form = RecursoReporteForm(request.POST)

        if form.is_valid():
            aux = form.save(commit=False)
            lista1 = []
            if aux.estado and aux.tipo:
                lista1 = recurso.objects.filter(tipo=aux.tipo,estado=aux.estado).order_by('id')
            elif aux.estado:
                lista1 = recurso.objects.filter(estado=aux.estado).order_by('id')
            elif aux.tipo:
                lista1 = recurso.objects.filter(tipo=aux.tipo).order_by('id')
            else:
                lista1 = recurso.objects.all().order_by('id')

            listafinal = []
            listaaux = usuario.objects.all()

            for recursos in lista1:
                for usuarios in listaaux:
                    for rol in usuarios.rol.all():
                        if recursos.tipo == rol.tipoRecurso:
                            var = datos(recursos.id, recursos.nombre, recursos.tipo, recursos.estado, usuarios.nombres)
                            listafinal.append(var)

            context = {'recursos': listafinal}
            pdf = render_to_pdf('recurso/reporteRecurso.html', context)
            if pdf:
                return HttpResponse(pdf, content_type='application/pdf')
            return HttpResponse("No se encontraron los datos")

        return HttpResponse("Formulario no valido")

    else:
        form = RecursoReporteForm()
    return render(request, 'recurso/crearReporteRecurso.html', {'form': form})






def index(request):
    return render(request, 'usuario/index.html')

#--------------------------------------------RECURSO-----------------------------------
#--------------------------------------------------------------------------------------
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


#-----------------------------------------MANTENIMIENTO---------------------------------
#---------------------------------------------------------------------------------------
@permission_required('recurso.add_mantenimiento', login_url='/login/')
def crearMantenimiento_view(request, id_recurso):
    if request.method == 'POST':
        form = CrearMantenimientoForm(request.POST)
        if form.is_valid():
            man = form.save(commit=False)
            man.estado = estadoMantenimiento.objects.get(nombre="A realizar")
            man.cod_recurso = id_recurso
            man.save()
            var_recurso = recurso.objects.get(id=id_recurso)
            form1 = EditarRecursoForm(instance=var_recurso)
            rec = form1.save(commit=False)
            rec.mantenimiento = Mantenimiento.objects.get(estado=1,cod_recurso=id_recurso)
            rec.save()
            return redirect('recurso:listar_rec_man')

        return redirect('recurso:listar_recurso')
    else:
        form = CrearMantenimientoForm()

    return render(request,'recurso/crearMantenimiento_form.html', {'form': form})


@permission_required('recurso.change_mantenimiento', login_url='/login/')
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


@permission_required('recurso.ver_mantenimiento', login_url='/login/')
def listarMantenimiento_view(request): #lista los recursos y al lado tiene los links para asignar mantenimiento
    """despliega la lista de recursos registrados en el sistema de los tipos de recurso que el usuario administra"""
    lista = []
    for roldelusuario in request.user.rol.all():
        tiporecursodelusuario = roldelusuario.tipoRecurso
        nuevalista = Mantenimiento.objects.all().order_by('id')
        #print (nuevalista)
        for elemento in nuevalista:
            if(recurso.objects.get(id=elemento.cod_recurso).tipo == tiporecursodelusuario):
                lista.append(elemento)

    contexto = {'mantenimientos': lista}
    return render(request, 'recurso/listar_mantenimiento.html', contexto)


@permission_required('recurso.ver_mantenimiento', login_url='/login/')
def listarRecursoMantenimiento_view(request): #lista los recursos y con sus mantenimientos si es que tiene (mostrar)
    """despliega la lista de recursos registrados en el sistema de los tipos de recurso que el usuario administra"""
    lista = []
    for roldelusuario in request.user.rol.all():
        tiporecursodelusuario = roldelusuario.tipoRecurso
        nuevalista = recurso.objects.filter(tipo=tiporecursodelusuario).order_by('id')
        for elemento in nuevalista:
            #if (elemento.mantenimiento):
            #    print(elemento.mantenimiento.get_fecha_fin())
            lista.append(elemento)
    #lista = recurso.objects.all().order_by('id')
    contexto = {'recursos': lista, 'tiempo': datetime.combine(datetime.now().date(), datetime.now().time()).__str__()}
    #print(contexto['tiempo'])
    return render(request,'recurso/listar_rec_man.html', contexto)


@permission_required('recurso.ver_mantenimiento', login_url='/login/')
def listarAsignarMantenimiento_view(request): #lista para asignar el mantenimiento
    lista = []
    for roldelusuario in request.user.rol.all():
        tiporecursodelusuario = roldelusuario.tipoRecurso
        nuevalista = recurso.objects.filter(tipo=tiporecursodelusuario).order_by('id')
        for elemento in nuevalista:
            lista.append(elemento)
    #lista = recurso.objects.all().order_by('id')
    contexto = {'recursos': lista}
    return render(request, 'recurso/listar_asignar_man.html', contexto)


#--------------------------------------TIPO RECURSO-------------------------------------
#---------------------------------------------------------------------------------------
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
    lista1 = []
    for roldelusuario in request.user.rol.all():
        if(roldelusuario.tipoRecurso):
            tiporecursodelusuario = roldelusuario.tipoRecurso
            lista1.append(tiporecursodelusuario)
    #lista1 = Tipo_de_recurso.objects.all().order_by('id')
    contexto1 = {'tipos': lista1}
    return render(request,'recurso/listar_tiporecurso.html', contexto1)


@permission_required('recurso.delete_tipo_de_recurso', login_url='/login/')
def eliminarTipoRecurso_view(request, id_Tipo_de_recurso):
    """borra un Tipo de Recurso registrado de la base de datos del sistema"""
    var_Tipo_de_recurso = Tipo_de_recurso.objects.get(id=id_Tipo_de_recurso)
    if request.method == 'POST':
        var_Tipo_de_recurso.delete()
        return redirect('recurso:listar_tiporecurso')
    return render(request,'recurso/eliminar_tiporecurso.html', {'Tipo_de_recurso_aux': var_Tipo_de_recurso})



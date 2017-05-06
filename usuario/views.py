from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from forms import UsuarioForm, CrearRolForm, EditarRolForm, EditarUsuarioForm
from models import rol, usuario


# Create your views here.


def index(request):
    return render(request, 'usuario/index.html')


def crearRol_view(request):
    if request.method == 'POST':
        form = CrearRolForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('login_page')
            # return redirect('usuario: index')
    else:
        form = CrearRolForm()

    return render(request, 'usuario/crearrol_form.html', {'form': form})


def listarRol_view(request):
    lista = rol.objects.all().order_by('id')
    contexto = {'roles': lista}
    return render(request, 'usuario/listar_rol.html', contexto)

def editarRol_view(request, id_rol):

    var_rol = rol.objects.get(id=id_rol)
    if request.method == 'GET':
        form = EditarRolForm(instance=var_rol)
    else:
        form = EditarRolForm(request.POST, instance=var_rol)
        if form.is_valid():
            form.save()
        return redirect('usuario:listar_rol')
    return render(request, 'usuario/crearrol_form.html', {'form': form})

def eliminarRol_view(request, id_rol):

    var_rol = rol.objects.get(id=id_rol)
    if request.method == 'POST':
        var_rol.delete()
        return redirect('usuario:listar_rol')
    return render(request,'usuario/eliminar_rol.html', {'rol_aux': var_rol})




def crearUsuario_view(request):
    if request.method == 'POST':
        f = UsuarioForm(request.POST)
        if f.is_valid():
            new_author = f.save(commit=False)
            new_author.password = make_password(new_author.password)
            new_author.save()
            f._save_m2m()
            #guardar permisos en el usuario
            objetorol = rol.objects.latest('nombre')
            objetousuario = usuario.objects.latest('username')

            for objetopermiso in objetorol.permisos.all():
                objetousuario.user_permissions.add(objetopermiso)

            return redirect('login_page')
        return redirect('usuario: index')
    else:
        form = UsuarioForm()

    return render(request,'usuario/usuario_form.html', {'form': form})

def listarUsuario_view(request):
    """despliega una lista de usuarios registrados en el sistema"""
    lista = usuario.objects.all().order_by('id')
    contexto = {'usuarios':lista}
    return render(request,'usuario/listar_usuario.html', contexto)


def editarUsuario_view(request, id_usuario):
    """permite modificar los atributos del modelo usuario"""
    var_usuario = usuario.objects.get(id=id_usuario)
    if request.method == 'GET':
        form = EditarUsuarioForm(instance=var_usuario)
    else:
        form = EditarUsuarioForm(request.POST, instance=var_usuario)
        if form.is_valid():
            form.save()
        return redirect('usuario:listar_usuario')
    return render(request, 'usuario/usuario_form.html', {'form': form})


def eliminarUsuario_view(request, id_usuario):
    """borra un usuario registrado en la base de datos del sistema"""
    var_usuario = usuario.objects.get(id=id_usuario)
    if request.method == 'POST':
        var_usuario.delete()
        return redirect('usuario:listar_usuario')
    return render(request,'usuario/eliminar_usuario.html', {'usuario_aux': var_usuario})

"""
def modificarRol_view(request):
    if request.method == 'POST':
        form = ModificarRolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('modificar_rol')
        #return redirect('usuario: index')
    else:
        form = ModificarRolForm()

    return render(request,'usuario/crearrol_form.html', {'form': form})

"""
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from forms import UsuarioForm, CrearRolForm,EditarUsuarioForm
# Create your views here.
from models import usuario


def index(request):
    return render(request, 'usuario/index.html')

def crearUsuario_view(request):
    if request.method == 'POST':
        f = UsuarioForm(request.POST)
        if f.is_valid():
            new_author = f.save(commit=False)
            new_author.password = make_password(new_author.password)
            new_author.save()
            f._save_m2m()
            return redirect('login_page')
        return redirect('usuario: index')
    else:
        form = UsuarioForm()

    return render(request,'usuario/usuario_form.html', {'form': form})


def crearRol_view(request):
    if request.method == 'POST':
        form = CrearRolForm(request.POST)
        if form.is_valid():
            form.save()
            #return redirect('login_page')
        #return redirect('usuario: index')
    else:
        form = CrearRolForm()

    return render(request,'usuario/crearrol_form.html', {'form': form})

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
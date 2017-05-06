from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from forms import UsuarioForm, CrearRolForm, ModificarRolForm
from models import rol, usuario
from django.views.generic import UpdateView
from django.core.urlresolvers import reverse_lazy
# Create your views here.


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

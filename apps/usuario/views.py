from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from forms import UsuarioForm, CrearRolForm
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


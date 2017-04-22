from django.shortcuts import render, redirect

from django.contrib.auth.hashers import make_password

from forms import CrearRecursoForm
# Create your views here.


def index(request):
    return render(request, 'usuario/index.html')


def crearRecurso_view(request):
    if request.method == 'POST':
        form = CrearRecursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_page')
        return redirect('usuario: index')
    else:
        form = CrearRecursoForm()

    return render(request,'recurso/crearRecurso_form.html', {'form': form})


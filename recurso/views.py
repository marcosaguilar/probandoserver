from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required, login_required
from forms import CrearRecursoForm
# Create your views here.

from models import EstadoRecurso#, Mantenimiento


def index(request):
    return render(request, 'usuario/index.html')


@permission_required('recurso.add_recurso')
def crearRecurso_view(request):
    if request.method == 'POST':
        form = CrearRecursoForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.estado = EstadoRecurso.objects.get(estado='Disponible')
            #form.mantenimiento = Mantenimiento.objects.get(estado='Sin tipo')
            form.save()
            return redirect('login_page')
        return redirect('usuario: index')
    else:
        form = CrearRecursoForm()

    return render(request,'recurso/crearRecurso_form.html', {'form': form})


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from forms import CrearReservaForm, EditarReservaForm
from models import reserva, estadoReserva

# Create your views here.

#----------------------------------RESERVAS-------------------------------------------
#-------------------------------------------------------------------------------------
@permission_required('reserva.add_reserva', login_url='/login/')
def crearReserva_view(request):
    """crea una reserva en el sistema"""
    if request.method == 'POST':
        form = CrearReservaForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.tipo_recurso = form.recurso.tipo
            form.usuario = request.user
            form.estado_reserva = estadoReserva.objects.get(estado="A confirmar")
            form.save()
            return redirect('/reserva/listarreserva')
    else:
        form = CrearReservaForm()

    return render(request, 'reserva/crearReserva_form.html', {'form': form})


@permission_required('reserva.ver_reserva', login_url='/login/')
def listarReserva_view(request):
    """despliega una lista de reservas registradas en el sistema"""
    lista1 = reserva.objects.all().order_by('id')
    contexto1 = {'reservas': lista1}
    return render(request,'reserva/listarReserva_form.html', contexto1)


@permission_required('reserva.change_reserva', login_url='/login/')
def editarReserva_view(request, id_reserva):
    """permite modificar los atributos de una reserva"""
    var_reserva = reserva.objects.get(id=id_reserva)
    if request.method == 'GET':
        form = EditarReservaForm(instance=var_reserva)
    else:
        form = EditarReservaForm(request.POST, instance=var_reserva)
        if form.is_valid():
            form.save()
        return redirect('reserva:listar_reserva')
    return render(request, 'reserva/crearReserva_form.html', {'form': form})


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from forms import CrearReservaForm, EditarReservaForm
from models import reserva, estadoReserva, listaReserva
from datetime import datetime, timedelta
from recurso.models import recurso

# Create your views here.

#----------------------------------RESERVAS-------------------------------------------
#-------------------------------------------------------------------------------------
@permission_required('reserva.add_reserva', login_url='/login/')
def crearReserva_view(request):
    """crea una reserva en el sistema"""
    if request.method == 'POST':
        form = CrearReservaForm(request.POST)
        if form.is_valid():
            nosepudoreservar = False
            form = form.save(commit=False)
            form.tipo_recurso = form.recurso.tipo
            form.usuario = request.user
            form.estado_reserva = estadoReserva.objects.get(estado="A confirmar")
            #ver si entra en lista o es directa
            #si es menos de 48 hs
            fechainicio = datetime.strptime(form.fecha_inicio, '%Y-%m-%d %H:%M') #convierte a tipo datetime
            fechafinal = datetime.strptime(form.fecha_fin, '%Y-%m-%d %H:%M')
            if(fechainicio.date().__str__() <= (datetime.now().date()+timedelta(days=2)).__str__()):
                #busca lista de reserva de ese recurso y fecha igual
                listaencontrada = False
                for listareserva in listaReserva.objects.all():
                    if (listareserva.recurso == form.recurso and fechainicio.date().__str__() == listareserva.fecha):
                        listaencontrada = True
                        break
                #si encuentra busca entre las reservas ganadoras y compara sus horas
                if(listaencontrada):
                    puedereservar = True
                    for reserva1 in reserva.objects.filter(lista_reserva=listareserva):
                        if(reserva1.gano_reserva):
                            if(reserva1.fecha_inicio <= fechainicio.__str__() and
                            reserva1.fecha_fin >= fechainicio.__str__() or
                            reserva1.fecha_inicio <= fechafinal.__str__() and
                            reserva1.fecha_fin >= fechafinal.__str__()):
                                puedereservar = False
                                break
                    if (puedereservar):
                        form.lista_reserva = listareserva
                        form.gano_reserva = True
                    else:
                        nosepudoreservar = True
                #si no crea una lista y reserva directamente
                else:
                    form.lista_reserva = listaReserva.objects.create(fecha=fechainicio.date().__str__(), recurso=form.recurso)
                    form.gano_reserva = True
            #si es mas de 48 hs
            else:
                listaencontrada = False
                #busca lista de reserva de ese recurso y fecha igual
                for listareserva in listaReserva.objects.all():
                    if (listareserva.recurso == form.recurso and fechainicio.date().__str__() == listareserva.fecha):
                        listaencontrada = True
                        break
                #si encuentra entra en la lista
                if (listaencontrada):
                    form.lista_reserva = listareserva
                #si no crea una lista reserva
                else:
                    form.lista_reserva = listaReserva.objects.create(fecha=fechainicio.date().__str__(), recurso=form.recurso)
            if (not nosepudoreservar):
                form.save()
                return redirect('/reserva/listarreserva')
            else:
                #agregar pagina con mensaje de que no se pudo crear
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


def listarListaReserva_view(request):
    """despliega una lista de listas de reservas registradas en el sistema"""
    lista1 = listaReserva.objects.all().order_by('id')
    contexto1 = {'listas': lista1}
    return render(request,'reserva/listarListaReserva_form.html', contexto1)


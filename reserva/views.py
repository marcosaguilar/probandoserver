from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from forms import CrearReservaForm, EditarReservaForm, CrearReservaGeneralForm
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
            form.fechayhora = datetime.now().__str__()
            form.gano_reserva = 0
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
                        form.gano_reserva = 2
                    else:
                        nosepudoreservar = True
                #si no crea una lista y reserva directamente
                else:
                    form.lista_reserva = listaReserva.objects.create(fecha=fechainicio.date().__str__(), recurso=form.recurso)
                    form.gano_reserva = 2
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


#-------------------------------------LISTARESERVA-----------------------------------------
#------------------------------------------------------------------------------------------
def listarListaReserva_view(request):
    """despliega una lista de listas de reservas registradas en el sistema"""
    lista1 = listaReserva.objects.all().order_by('id')
    contexto1 = {'listas': lista1}
    return render(request,'reserva/listarListaReserva_form.html', contexto1)


def calcular_view(request, id_lista):
    seguir = True
    while (seguir):
        seguir = False
        ganador = False

        for reserva1 in reserva.objects.all():  #si la reserva se encuentra en la lista y esta sin determinar, es ganadora para empezar
            if (reserva1.lista_reserva_id.__str__() == id_lista.__str__() and reserva1.gano_reserva == 0):
                ganador = reserva1
                break

        if (ganador):
            for reserva1 in reserva.objects.all():
                if (reserva1.lista_reserva_id.__str__() == id_lista.__str__() and reserva1.gano_reserva == 0):
                    seguir = True           #continua si alguno sin gano_reserva
                    if(reserva1.usuario.prioridad > ganador.usuario.prioridad):
                        ganador = reserva1
                    elif(reserva1.usuario.prioridad == ganador.usuario.prioridad):
                        if(reserva1.fechayhora < ganador.fechayhora):
                            ganador = reserva1
            ganador.gano_reserva = 2
            ganador.save()

            for reserva1 in reserva.objects.all():  #pierden la reserva los que estan a la misma hora
                if (reserva1.lista_reserva_id.__str__() == id_lista.__str__() and reserva1.gano_reserva == 0):
                    if (reserva1.id.__str__() != ganador.id.__str__()):
                        if (reserva1.fecha_inicio.__str__() >= ganador.fecha_inicio.__str__() and   #el inicio entre el ganador
                                reserva1.fecha_inicio.__str__() <= ganador.fecha_fin.__str__() or
                                reserva1.fecha_fin.__str__() >= ganador.fecha_inicio.__str__() and  #el final entre el ganador
                                reserva1.fecha_fin.__str__() <= ganador.fecha_fin.__str__() or
                                ganador.fecha_inicio.__str__() >= reserva1.fecha_inicio and         #el ganador dentro
                                ganador.fecha_fin.__str__() <= reserva1.fecha_fin.__str__()):
                            reserva1.gano_reserva = 1   #perdieron los que compiten con el ganador
                            reserva1.save()

    return render(request,'inicio.html')


@permission_required('reserva.add_reserva', login_url='/login/')
def crearReservaGeneral_view(request):
    """crea una reserva general en el sistema"""
    if request.method == 'POST':
        form = CrearReservaGeneralForm(request.POST)
        if form.is_valid():
            nosepudoreservar = False
            form = form.save(commit=False)
            form.usuario = request.user
            form.estado_reserva = estadoReserva.objects.get(estado="A confirmar")
            form.fechayhora = datetime.now().__str__()
            form.gano_reserva = 0
            #comprobar si es directa
            fechainicio = datetime.strptime(form.fecha_inicio, '%Y-%m-%d %H:%M') #convierte a tipo datetime
            fechafinal = datetime.strptime(form.fecha_fin, '%Y-%m-%d %H:%M')
            if(fechainicio.date().__str__() <= (datetime.now().date()+timedelta(days=2)).__str__()):
                #for recursos del tipo de recurso
                for recurso1 in recurso.objects.all(): #falta break y si no encontro
                    if (recurso1.tipo == form.tipo_recurso):
                        nosepudoreservar = False
                        #busca lista de reserva de ese recurso y fecha igual
                        listaencontrada = False
                        for listareserva in listaReserva.objects.all():
                            if (listareserva.recurso == recurso1 and fechainicio.date().__str__() == listareserva.fecha):
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
                                form.gano_reserva = 2
                                break
                            else:
                                nosepudoreservar = True
                        #si no crea una lista y reserva directamente
                        else:
                            form.lista_reserva = listaReserva.objects.create(fecha=fechainicio.date().__str__(), recurso=recurso1)
                            form.gano_reserva = 2
                            break
                    else:
                        nosepudoreservar = True
            else:
                nosepudoreservar = True
            if (not nosepudoreservar):
                form.recurso = recurso1
                form.save()
                return redirect('/reserva/listarreserva')
            else:
                #agregar pagina con mensaje de que no se pudo crear
                return redirect('/reserva/listarreserva')
    else:
        form = CrearReservaGeneralForm()

    return render(request, 'reserva/crearReserva_form.html', {'form': form})


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from forms import CrearReservaForm, EditarReservaForm, CrearReservaGeneralForm
from models import reserva, estadoReserva, listaReserva
from datetime import datetime, timedelta
from recurso.models import recurso
from django.conf import settings
from django.core.mail import send_mail

#--------------------------------------------Reportes-----------------------------------
#--------------------------------------------------------------------------------------

from forms import ReservaReporteForm
from probandoserver.views import render_to_pdf
from usuario.models import rol, usuario



from django.http import HttpResponse

class datos:
    id = ""
    nomrec = ""
    tipo = ""
    estado = ""
    resp = ""
    fecha =""
    #nomuser = ""

    #def __init__(self, a, b,c,d,e,f,g):

    #    self.id = a
    #    self.nomrec = b
    #    self.tipo = c
    #    self.estado = d
    #    self.resp = e
    #    self.fecha = f
    #    self.nomuser = g

    def __init__(self, a, b, c, d, f,g):
        self.id = a
        self.nomrec = b
        self.tipo = c
        self.estado = d
        #self.resp = e
        self.fecha = f
        self.nomuser = g

def encontrarresponsables(varreserva):
    """genera una lista de usuarios que estan asociados a los tipos de recursos segun sus roles"""
    lista =[]
    listauser = usuario.objects.all()

    for usuarios in listauser:
        for rol in usuarios.rol.all():
            if rol.tipoRecurso == varreserva.tipo_recurso:
                lista.append(usuarios)
    return lista


def crear_reporte(request):
    """genera los datos para el reporte de las reservas """

    if request.method == 'POST':
        form = ReservaReporteForm(request.POST)
        if form.is_valid():
            aux = form.save(commit=False)
            lista1 = reserva.objects.all()
            if aux.estado_reserva and aux.tipo_reserva:
                lista1 = reserva.objects.filter(estado_reserva=aux.estado_reserva,tipo_reserva=aux.tipo_reserva).order_by('id')
            elif aux.estado_reserva:
                lista1 = reserva.objects.filter(estado_reserva=aux.estado_reserva).order_by('id')
            elif aux.tipo_reserva:
                lista1 = reserva.objects.filter(tipo_reserva=aux.tipo_reserva).order_by('id')

            lista2 = []
            if aux.fecha_fin and aux.fecha_inicio:


                print ("entra en la lista ")


                for reservas in lista1:
                    if aux.fecha_inicio.__str__() <= reservas.fecha_inicio.__str__() and reservas.fecha_fin.__str__() <= aux.fecha_fin.__str__():
                        lista2.append(reservas)
            else:
                lista2 = lista1

            listafinal = []

            for res in lista2:
                #listauser = encontrarresponsables(res)
                #for user in listauser:
                    #var=datos(res.recurso.id,res.recurso.nombre,res.recurso.tipo,res.estado_reserva,user.nombres,res.fechayhora,res.usuario.nombres)
                var = datos(res.recurso.id, res.recurso.nombre, res.recurso.tipo, res.estado_reserva,
                            res.fechayhora, res.usuario.nombres)

                listafinal.append(var)

            for n in listafinal:
                print(n.nomrec)

            context = {'reservas': listafinal}
            pdf = render_to_pdf('reserva/reporteReserva.html', context)
            if pdf:
                return HttpResponse(pdf, content_type='application/pdf')
            return HttpResponse("No se encontraron los datos")

        return HttpResponse("Formulario no valido")

    else:
        form = ReservaReporteForm()
    return render(request, 'recurso/crearReporteRecurso.html', {'form': form})

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
            print (var_reserva.estado_reserva)
            if var_reserva.estado_reserva.estado == "Cancelado":

                subject = 'Reserva cancelada'
                message = 'Su reserva ha sido cancelada.\n\nSaludos.\n\nEl equipo de desarrollo'
                from_email = settings.EMAIL_HOST
                print (var_reserva.usuario.email)
                to_list = [var_reserva.usuario.email]
                send_mail(subject, message, from_email, to_list, fail_silently=False)



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

            subject = 'Reserva Confirmada'
            message = 'Su reserva ha sido confirmada.\n\nSaludos.\n\nEl equipo de desarrollo'
            from_email = settings.EMAIL_HOST
            to_list = [ganador.usuario.email]

            send_mail(subject, message, from_email, to_list, fail_silently=False)

            for reserva1 in reserva.objects.all():  #pierden la reserva los que estan a la misma hora
                if (reserva1.lista_reserva_id.__str__() == id_lista.__str__() and reserva1.gano_reserva == 0):
                    perdedor=reserva1
                    if (perdedor.id.__str__() != ganador.id.__str__()):
                        if (perdedor.fecha_inicio.__str__() >= ganador.fecha_inicio.__str__() and   #el inicio entre el ganador
                                perdedor.fecha_inicio.__str__() <= ganador.fecha_fin.__str__() or
                                perdedor.fecha_fin.__str__() >= ganador.fecha_inicio.__str__() and  #el final entre el ganador
                                perdedor.fecha_fin.__str__() <= ganador.fecha_fin.__str__() or
                                perdedor.fecha_inicio.__str__() >= reserva1.fecha_inicio and         #el ganador dentro
                                perdedor.fecha_fin.__str__() <= reserva1.fecha_fin.__str__()):
                            perdedor.gano_reserva = 1   #perdieron los que compiten con el ganador
                            perdedor.save()
                            subject = 'Reserva cancelada'
                            message = 'Su reserva ha sido cancelada.\n\nSaludos.\n\nEl equipo de desarrollo'
                            from_email = settings.EMAIL_HOST
                            to_list = [perdedor.usuario.email]
                            send_mail(subject, message, from_email, to_list, fail_silently=False)

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


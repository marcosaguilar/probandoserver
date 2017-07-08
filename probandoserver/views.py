# from django.template import RequestContext
from django.shortcuts import render, redirect
from forms import LoginForm
from django.contrib.auth import authenticate, login, logout

from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


#from django.views.generic import View

def render_to_pdf(template_src, context_dict={}):
    """convierte el reporte en html a pdf"""
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None



def login_page(request):
    message = None
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            usuario = authenticate(username=username, password=password)
            if usuario is not None:
                if usuario.is_active:
                    login(request, usuario)
                    message = "te has identificado"
                    for permiso in usuario.user_permissions.all():
                        if(permiso.codename == "ver_mantenimiento"):
                            return redirect('recurso/listarrecursoymantenimiento')
                else:
                    message = "incorrecto"
            else:
                message = "nombre de usuario o contrasena incorrecta"
        else:
            message = "form no es valido"
    else:
        form = LoginForm()
    return render(request, 'login.html', {'message': message, 'form': form})


def homepage(request):
    return render(request,'inicio.html')


def logout_page(request):
    message = None
    if request.user.is_authenticated:
        message = "Sesion cerrada"
    else:
        message = "No has iniciado sesion"
    logout(request)
    return render(request, 'logout.html', {'message': message})


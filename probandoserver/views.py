# from django.template import RequestContext
from django.shortcuts import render, redirect
from forms import LoginForm
from django.contrib.auth import authenticate, login


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
                    #return redirect('inicio.html') #no se si esta bien, verificar
                else:
                    message = "incorrecto"
            else:
                message = "nombre de usuario o contrasena incorrecta"
        else:
            message = "form no es valido"
    else:
        form = LoginForm()
    return render(request, 'login.html', {'message': message, 'form': form})

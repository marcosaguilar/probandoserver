from django.shortcuts import render, redirect

from forms import UsuarioForm
# Create your views here.


def index(request):
    return render(request, 'usuario/index.html')

def usuario_view(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('usuario:index')
    else:
        form=UsuarioForm()

    return render(request,'usuario/usuario_form.html',{'form':form})
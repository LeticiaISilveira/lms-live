from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from .forms import ContatoForm


def home(request):
    return render(request, 'index.html')


def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.enviar_email()
            return redirect('/')
    else:
        form = ContatoForm()

    return render(
        request,
        'contato.html',
        {
            'form': form
        })


def entrar(request):
    erro = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(request, username=username, password=password)
        if usuario:
            login(request, usuario)
            return redirect('/restrito/')
        else:
            erro = 'Usuário ou senha incorretos'

    return render(request, 'entrar.html', {'erro': erro})


def sair(request):
    logout(request)
    return redirect('/')

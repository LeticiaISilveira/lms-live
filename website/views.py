from django.shortcuts import redirect, render
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

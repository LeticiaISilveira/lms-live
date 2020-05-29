from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import CursoForm
from .models import Curso


@login_required
def home(request):
    cursos = Curso.objects.all()
    return render(request, 'restrito/index.html', {'cursos': cursos})


@login_required
def curso_form(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/restrito/')
    else:
        form = CursoForm()

    return render(request, 'restrito/curso_form.html', {'form': form})

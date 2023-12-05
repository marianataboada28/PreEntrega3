from django.shortcuts import render, redirect
from .models import Curso
from .forms import CursoForm, BusquedaForm

def home(request):
    return render(request, 'cursos/home.html')

def agregar_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_cursos')
    else:
        form = CursoForm()
    return render(request, 'cursos/agregar_curso.html', {'form': form})

def buscar_cursos(request):
    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            busqueda = form.cleaned_data['busqueda']
            cursos = Curso.objects.filter(nombre__icontains=busqueda)
            return render(request, 'cursos/lista_cursos.html', {'cursos': cursos, 'busqueda': busqueda})
    else:
        form = BusquedaForm()
    return render(request, 'cursos/buscar_cursos.html', {'form': form})

def lista_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos/lista_cursos.html', {'cursos': cursos})



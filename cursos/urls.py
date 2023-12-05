# cursos/urls.py
from django.urls import path
from .views import home, agregar_curso, buscar_cursos, lista_cursos

urlpatterns = [
    path('', home, name='home'),
    path('agregar/', agregar_curso, name='agregar_curso'),
    path('buscar/', buscar_cursos, name='buscar_cursos'),
    path('lista/', lista_cursos, name='lista_cursos'),
]
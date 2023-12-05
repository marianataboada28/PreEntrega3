# Proyecto Web Django con MVT

Este proyecto implementa un sistema simple de cursos utilizando el patrón MVT en Django.

## Instrucciones para ejecutar el proyecto

1. Clona este repositorio.
2. Crea un entorno virtual y activa.
3. Instala las dependencias: `pip install -r requirements.txt`.
4. Aplica las migraciones: `python manage.py makemigrations` y `python manage.py migrate`.
5. Ejecuta el servidor: `python manage.py runserver`.

## Orden para probar las funcionalidades

1. Agregar un curso: Visita `http://localhost:8000/cursos/agregar_curso/` y completa el formulario.
2. Buscar cursos: Visita `http://localhost:8000/cursos/buscar_cursos/` y utiliza el formulario de búsqueda.
3. Ver la lista de cursos: Visita `http://localhost:8000/cursos/lista_cursos/` para ver todos los cursos.

¡Disfruta explorando el proyecto!

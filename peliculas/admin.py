from django.contrib import admin
from .models import Pelicula


@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'director', 'anio', 'genero', 'calificacion']
    list_filter = ['genero', 'anio']
    search_fields = ['titulo', 'director']

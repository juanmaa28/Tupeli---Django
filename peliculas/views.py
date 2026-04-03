from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Pelicula
from .forms import PeliculaForm


def lista_peliculas(request):
    peliculas = Pelicula.objects.all()
    return render(request, 'peliculas/lista.html', {'peliculas': peliculas})


def detalle_pelicula(request, pk):
    pelicula = get_object_or_404(Pelicula, pk=pk)
    return render(request, 'peliculas/detalle.html', {'pelicula': pelicula})


def crear_pelicula(request):
    if request.method == 'POST':
        form = PeliculaForm(request.POST)
        if form.is_valid():
            pelicula = form.save()
            messages.success(request, f'Película "{pelicula.titulo}" creada exitosamente.')
            return redirect('lista_peliculas')
    else:
        form = PeliculaForm()
    return render(request, 'peliculas/formulario.html', {'form': form, 'titulo': 'Agregar Película'})


def editar_pelicula(request, pk):
    pelicula = get_object_or_404(Pelicula, pk=pk)
    if request.method == 'POST':
        form = PeliculaForm(request.POST, instance=pelicula)
        if form.is_valid():
            form.save()
            messages.success(request, f'Película "{pelicula.titulo}" actualizada exitosamente.')
            return redirect('lista_peliculas')
    else:
        form = PeliculaForm(instance=pelicula)
    return render(request, 'peliculas/formulario.html', {'form': form, 'titulo': 'Editar Película', 'pelicula': pelicula})


def eliminar_pelicula(request, pk):
    pelicula = get_object_or_404(Pelicula, pk=pk)
    if request.method == 'POST':
        titulo = pelicula.titulo
        pelicula.delete()
        messages.success(request, f'Película "{titulo}" eliminada exitosamente.')
        return redirect('lista_peliculas')
    return render(request, 'peliculas/confirmar_eliminar.html', {'pelicula': pelicula})

from django import forms
from .models import Pelicula

INPUT_CLASS = 'w-full px-3 py-2.5 bg-zinc-800 border border-zinc-700 text-white rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-transparent placeholder-zinc-500 text-sm'


class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ['titulo', 'director', 'anio', 'genero', 'sinopsis', 'imagen_url', 'calificacion']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': INPUT_CLASS,
                'placeholder': 'Titulo de la pelicula',
            }),
            'director': forms.TextInput(attrs={
                'class': INPUT_CLASS,
                'placeholder': 'Nombre del director',
            }),
            'anio': forms.NumberInput(attrs={
                'class': INPUT_CLASS,
                'placeholder': '2024',
                'min': 1888,
                'max': 2100,
            }),
            'genero': forms.Select(attrs={
                'class': INPUT_CLASS + ' bg-zinc-800',
            }),
            'sinopsis': forms.Textarea(attrs={
                'class': INPUT_CLASS,
                'rows': 4,
                'placeholder': 'Descripcion breve de la pelicula...',
            }),
            'imagen_url': forms.URLInput(attrs={
                'class': INPUT_CLASS,
                'placeholder': 'https://...',
            }),
            'calificacion': forms.NumberInput(attrs={
                'class': INPUT_CLASS,
                'step': '0.1',
                'min': '0',
                'max': '10',
                'placeholder': '0.0 - 10.0',
            }),
        }
        labels = {
            'titulo': 'Titulo',
            'director': 'Director',
            'anio': 'Año',
            'genero': 'Genero',
            'sinopsis': 'Sinopsis',
            'imagen_url': 'URL de la imagen (opcional)',
            'calificacion': 'Calificacion (0-10)',
        }

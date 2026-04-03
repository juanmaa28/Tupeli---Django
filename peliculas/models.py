from django.db import models


class Pelicula(models.Model):
    GENEROS = [
        ('accion', 'Acción'),
        ('comedia', 'Comedia'),
        ('drama', 'Drama'),
        ('terror', 'Terror'),
        ('ciencia_ficcion', 'Ciencia Ficción'),
        ('animacion', 'Animación'),
        ('romance', 'Romance'),
        ('thriller', 'Thriller'),
        ('documental', 'Documental'),
        ('otro', 'Otro'),
    ]

    titulo = models.CharField(max_length=200)
    director = models.CharField(max_length=150)
    anio = models.PositiveIntegerField()
    genero = models.CharField(max_length=50, choices=GENEROS)
    sinopsis = models.TextField()
    imagen_url = models.URLField(blank=True, null=True)
    calificacion = models.DecimalField(max_digits=3, decimal_places=1)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} ({self.anio})"

    class Meta:
        ordering = ['-anio']
        verbose_name = 'Película'
        verbose_name_plural = 'Películas'

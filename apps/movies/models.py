from django.db import models
from django.urls import reverse_lazy


# Create your models here.

class BaseName(models.Model):
    name = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Categories(BaseName):
    minimum_age = models.IntegerField()

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class Movies(BaseName):
    description = models.CharField(max_length=256)
    image = models.ImageField(upload_to='movies')
    release_date = models.DateField()
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Pelicula'
        verbose_name_plural = 'Peliculas'

    def get_edit_url(self):
        return reverse_lazy('movies:movies-edit', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse_lazy('movies:movies-delete', kwargs={'pk': self.pk})

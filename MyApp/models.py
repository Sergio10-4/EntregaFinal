from django.db import models
from django.core.validators import MaxLengthValidator
from django.contrib.auth.models import User

# Create your models here.

class Tag(models.Model):

    GENEROS = (
        ('Accion', 'Acción'),
        ('Comedia', 'Comedia'),
        ('Drama', 'Drama'),
        ('Fantasia', 'Fantasía'),
        ('Animacion', 'Animacion'),
        ('Terror', 'Terror'),
        ('Thriller', 'Thriller'),
        ('Suspenso', 'Suspenso'),
        ('Sci-Fi', 'Sci-Fi'),
        # Agrega más géneros según tus necesidades
    )

    nombre = models.CharField(max_length=100, choices=GENEROS)

    def __str__(self):
        return f' {self.nombre}'
    
    class Meta():

        verbose_name = 'Generos'
        verbose_name_plural = 'Generos De Cine'
        ordering = ('nombre',)


class Productora(models.Model):

    nombre = models.CharField(max_length=100, unique=True)
    año_fundacion = models.DateField()
    historia = models.TextField(null=True, validators=[MaxLengthValidator(250)])
    sede = models.ImageField(null=True)
    valoracion = models.URLField(null=True)

    def __str__(self):
        return f' {self.nombre} - {self.año_fundacion} - {self.historia} - {self.sede}'
    
    class Meta():

        verbose_name = 'Productora'
        verbose_name_plural = 'Productoras De Cine'
        ordering = ('nombre',)

class Director(models.Model):

    nombre = models.CharField(max_length=100)
    año_debut = models.DateField()
    edad = models.IntegerField()
    avatar = models.ImageField(null=True)

    def __str__(self):
        return f' {self.nombre} - {self.año_debut} - {self.edad}- {self.avatar}'
    
    class Meta():

        verbose_name = 'Director'
        verbose_name_plural = 'Directores De Cine'
        ordering = ('nombre',)


class Pelicula(models.Model):

    nombre = models.CharField(max_length=100)
    rating = models.IntegerField(null=True)
    tags = models.ManyToManyField(Tag)
    descripcion = models.TextField(null=True, validators=[MaxLengthValidator(250)])
    reseña = models.TextField(null=True, validators=[MaxLengthValidator(250)])
    portada = models.ImageField(null=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    productoraCinematografica = models.ForeignKey(Productora, on_delete=models.CASCADE)
    valoracion = models.URLField(null=True)

    def __str__(self):
        return f' {self.nombre} - {self.rating} - {self.tags} - {self.descripcion} - {self.reseña} - {self.portada} - {self.director} - {self.productoraCinematografica} - {self.valoracion}'        
    
    class Meta():

        verbose_name = 'Pelicula'
        verbose_name_plural = 'Catalogo De Peliculas'
        ordering = ('nombre',)

class Serie(models.Model):

    nombre = models.CharField(max_length=100)
    rating = models.IntegerField(null=True)
    tags = models.ManyToManyField(Tag)
    descripcion = models.TextField(null=True, validators=[MaxLengthValidator(250)])
    reseña = models.TextField(null=True, validators=[MaxLengthValidator(250)])
    portada = models.ImageField(null=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    productoraCinematografica = models.ForeignKey(Productora, on_delete=models.CASCADE)
    valoracion = models.URLField(null=True)

    def __str__(self):
        return f' {self.nombre} - {self.rating} - {self.tags} - {self.descripcion} - {self.reseña} - {self.portada} - {self.director} - {self.productoraCinematografica}- {self.valoracion}'
        
    class Meta():

        verbose_name = 'Serie'
        verbose_name_plural = 'Catalogo De Series'
        ordering = ('nombre',)


class fotoPerfil(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='FotoPerfil', null=True)
        
    class Meta():

        verbose_name = 'fotoPerfil'
        verbose_name_plural = 'FotosDePerfil'
        ordering = ('imagen',)
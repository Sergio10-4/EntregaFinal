from django.contrib import admin
from MyApp.models import Director, Productora, Pelicula, Serie, Tag
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import fotoPerfil

# Register your models here.

class ProductoraAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'año_fundacion', 'historia', 'sede', 'valoracion']
    search_fields = ['nombre', 'año_fundacion', 'historia', 'sede', 'valoracion']
    list_filter = ['nombre', 'año_fundacion', 'historia', 'sede', 'valoracion']

class PeliculaAdmin(admin.ModelAdmin):

    list_display = ['nombre', 'rating', 'tags', 'descripcion', 'reseña', 'portada', 'director', 'productoraCinematografica', 'valoracion']

    def tags(self, obj):
        return ', '.join(tag.nombre for tag in obj.tags.all())
    tags.short_description = 'Generos'

    search_fields = ['nombre', 'rating', 'tags', 'descripcion', 'reseña', 'portada', 'director', 'productoraCinematografica', 'valoracion']
    list_filter = ['nombre', 'rating', 'tags', 'descripcion', 'reseña', 'portada', 'director', 'productoraCinematografica', 'valoracion']


class SerieAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'rating', 'tags', 'descripcion', 'reseña', 'portada', 'director', 'productoraCinematografica', 'valoracion']

    def tags(self, obj):
        return ', '.join(tag.nombre for tag in obj.tags.all())
    tags.short_description = 'Generos'

    search_fields = ['nombre', 'rating', 'tags', 'descripcion', 'reseña', 'portada', 'director', 'productoraCinematografica', 'valoracion']
    list_filter = ['nombre', 'rating', 'tags', 'descripcion', 'reseña', 'portada', 'director', 'productoraCinematografica', 'valoracion']


class TagAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    search_fields = ['nombre']
    list_filter = ['nombre']

class DirectorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'año_debut', 'edad', 'avatar']
    search_fields = ['nombre', 'año_debut', 'edad', 'avatar']
    list_filter = ['nombre', 'año_debut', 'edad', 'avatar']

class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'get_foto_perfil')
    
    def get_foto_perfil(self, obj):
        foto = fotoPerfil.objects.filter(user=obj).first()
        if foto:
            return foto.imagen.url
        return ""
    get_foto_perfil.short_description = 'Foto de perfil'


admin.site.register(Productora, ProductoraAdmin)
admin.site.register(Pelicula, PeliculaAdmin)
admin.site.register(Serie, SerieAdmin)
admin.site.register(Director ,DirectorAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
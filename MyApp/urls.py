"""
URL configuration for EntregaCoder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.base, name="base"),
    path('home/', views.home, name="home"), 
    path('productos/', views.home, name="products"),
    path('main/', views.main, name="main"),
    path('iniciar-sesion/', views.inicioSesion, name="login"),
    path('registro/', views.register, name="register"), 
    path('cerrar-sesion/', views.cerrarSesion, name="logout"),
    path('perfil-usuario/', views.profile, name="perfil"),
    path('agregar-peliculas/', views.pelicula, name="AgregarPeliculas"),
    path('buscar-peliculas/', views.buscar_peliculas, name="buscarpelicula"),
    path('catalogo-de-peliculas/', views.peliCatalogo, name='catalogopeliculas'),
    path('agregar-serie/', views.serie, name="AgregarSeries"),
    path('buscar-serie/', views.buscar_series, name="buscarserie"),
    path('catalogo-de-series/', views.serieCatalogo, name='catalogoseries'),
    path('agregar-productoras/', views.productora, name="AgregarProductoras"),
    path('buscar-productoras/', views.buscar_productoras, name="buscarproductora"),
    path('catalogo-serie/', views.productoraCatalogo, name="catalogoproductoras"),
    path('lista-reseñas/', views.mostrar_reviews, name="ListadeReseñas"),
    path('Error-404/', views.Error, name="Error404"),
    path('sobre-la-pagina/', views.aboutPage, name="AboutPage"),
    path('sobre-sergio/', views.aboutSergio, name="AboutSergio"),
    path('sobre-maikol/', views.aboutMaikol, name="AboutMaikol"),
    path('actualizar-datos/', views.cambiarDatos, name="ActualizarPerfil"),
    path('password/', views.PasswordChange, name="cambiarContraseña"),
    path('actualizar-reseña-pelicula/<int:pelicula_id>/', views.Pelicula_reviewActualizar, name="actualizar_reseña_pelicula"),
]

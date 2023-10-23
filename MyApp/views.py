from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from MyApp.forms import CustomUserCreationForm, CustomUserUpdateForm, PeliculaForm, SerieForm, ProductoraForm, PeliculaResenaForm, SerieResenaForm
from django.contrib import messages
from MyApp.models import Productora, Pelicula, Serie, Tag
from django.views.generic.edit import UpdateView

# Create your views here.

def home(request):
    return render(request, 'home.html')

def inicioSesion(request):
    return render(request, 'inicio.html')

def register(request):
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'register.html', {'form': form})

def profile(request):
    return render(request, 'perfil.html')

def cerrarSesion(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('login')

def base(request):
    return render(request, 'base.html')

@login_required
def products(request):
    return render(request, 'productos.html')

def main(request):
    return render(request, 'main.html')

def cambiarDatos(request):
    if request.method == 'POST':
        form = CustomUserUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = CustomUserUpdateForm(instance=request.user)

    return render(request, 'editarPerfil.html', {'form': form})

def pelicula(request):
    if request.method == 'POST':
        formulario = PeliculaForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return render(request, 'main.html')
    else:
        formulario = PeliculaForm()

    context = {
        'form': formulario
    }
    return render(request, "peliculas.html", context)

def buscar_peliculas(request):
    query = request.GET.get('query', '')
    peliculas = Pelicula.objects.filter(nombre__icontains=query)
    generos = Tag.objects.filter(pelicula__in=peliculas).values('nombre')
    return render(request, 'resultadosBusqueda.html', {'peliculas': peliculas, 'generos': generos})

def peliCatalogo(request):
    return render(request, 'catalogoPeliculas.html')

def serie(request):
    if request.method == 'POST':
        formulario = SerieForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return render(request, 'main.html')
    else:
        formulario = SerieForm()

    context = {
        'form': formulario
    }
    return render(request, "series.html", context)

def buscar_series(req):
    query = req.GET.get('query', '')
    series = Serie.objects.filter(nombre__icontains=query)
    generos = Tag.objects.filter(serie__in=series).values('nombre')
    return render(req, 'resultadosbusquedaserie.html', {'series': series, 'query': query, 'generos': generos})

def serieCatalogo(request):
    return render(request, 'catalogoSeries.html')

def productora(req):
    if req.method == 'POST':
        formulario = ProductoraForm(req.POST)
        if formulario.is_valid():
            formulario.save()
            return render(req, 'main.html')
    else:
        formulario = ProductoraForm()
    return render(req, "productoras.html", {'form': formulario})

def buscar_productoras(req):
    query = req.GET.get('query', '')
    productoras = Productora.objects.filter(nombre__icontains=query)
    return render(req, 'resultadosbusquedaproductora.html', {'productoras': productoras, 'query': query})

def mostrar_reviews(request):

    series = Serie.objects.all()
    peliculas = Pelicula.objects.all()

    return render(request, 'mostrarReseñas.html', {'series': series, 'peliculas': peliculas})


def actualizar_review(request, pelicula_id):

    if request.method == 'POST':
        tipo = request.POST.get('tipo')
        id = request.POST.get('id')

        if tipo == 'pelicula':
            instancia = get_object_or_404(Pelicula, id=id)
            form = PeliculaResenaForm(request.POST, instance=instancia)
    
        elif tipo == 'serie':
            instancia = get_object_or_404(Serie, id=id)
            form = SerieResenaForm(request.POST, instance=instancia)
    
        else:
            messages.error(request, 'Dato Ingresado No Valido, Intentelo Denuevo')
            return redirect('ListadeReseñas')

        if form.is_valid():
            form.save()
            messages.success(request, 'Reseñas Actualizada Exitosamente')
            return redirect('perfil')

    else:
        messages.error(request, 'Método no permitido')
        return redirect('ListadeReseñas')

    peliculas = Pelicula.objects.all()
    series = Serie.objects.all()
    
    context = {
        'series': series,
        'peliculas': peliculas,
        'messages': messages.get_messages(request),  # Agregar esto al contexto
    }

    return render(request, 'mostrarReseñas.html', context)

    
def productoraCatalogo(request):
    return render(request, 'CatalogoProductoras.html')

def Error(request):
    return render(request, 'Error404.html')

def aboutPage(request):
    return render(request, 'aboutPage.html')

def aboutSergio(request):
    return render(request, 'aboutSergio.html')

def aboutMaikol(request):
    return render(request, 'aboutMaikol.html')
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate, update_session_auth_hash
from MyApp.forms import CustomUserCreationForm, CustomUserUpdateForm, PeliculaForm, SerieForm, ProductoraForm, PeliculaResenaForm, SerieResenaForm, PasswordChangeForm
from django.contrib import messages
from MyApp.models import Productora, Pelicula, Serie, Tag
from django.contrib.auth.models import User
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

def PasswordChange(request):
    user = request.user
    if request.method == 'POST':
        form = PasswordChangeForm(user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, '¡Contraseña cambiada exitosamente!')
            return redirect('perfil')
    else:
        form = PasswordChangeForm(user)
    return render(request, 'CambiarContraseña.html', {'form': form})

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


def Pelicula_reviewActualizar(request, pelicula_id):
    pelicula = get_object_or_404(Pelicula, id=pelicula_id)
    if request.method == 'POST':
        tipo = request.POST.get('tipo')
        id = request.POST.get('id')

        if tipo == 'pelicula' and int(id) == pelicula_id:
            instancia = get_object_or_404(Pelicula, id=id)
            form = PeliculaResenaForm(request.POST, instance=instancia)

            if form.is_valid():
                form.save()
                messages.success(request, 'Reseñas Actualizada Exitosamente')
                return redirect('perfil')
            else:
                messages.error(request, 'Error al actualizar la reseña de película')
        else:
            messages.error(request, 'Dato Ingresado NO Valido')
    else:
        messages.error(request, 'Metodo No Permitido')
    
    context = {
        'peliculas': [pelicula],
        'messages': messages.get_messages(request),
    }

    return render(request, 'actualizarReseñaPelicula.html', context)

    
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
from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.db import models
from MyApp.models import Productora, Pelicula, Tag, Serie, Director, fotoPerfil


class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class CustomUserUpdateForm(UserChangeForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class PasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = User


class ProductoraForm(forms.ModelForm):
    class Meta:
        model = Productora
        fields = ['nombre', 'año_fundacion', 'historia', 'sede', 'valoracion']


class PeliculaForm(forms.ModelForm):
    director = forms.ModelChoiceField(queryset=Director.objects.all(), empty_label=None)
    productoraCinematografica = forms.ModelChoiceField(queryset=Productora.objects.all(), empty_label=None)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['director'].label_from_instance = lambda obj: obj.nombre
        self.fields['productoraCinematografica'].label_from_instance = lambda obj: obj.nombre

    class Meta:
        model = Pelicula
        fields = ['nombre', 'rating', 'tags', 'descripcion', 'reseña', 'portada', 'director', 'productoraCinematografica', 'valoracion']

class SerieForm(forms.ModelForm):
    director = forms.ModelChoiceField(queryset=Director.objects.all(), empty_label=None)
    productoraCinematografica = forms.ModelChoiceField(queryset=Productora.objects.all(), empty_label=None)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['director'].label_from_instance = lambda obj: obj.nombre
        self.fields['productoraCinematografica'].label_from_instance = lambda obj: obj.nombre
    
    class Meta:
        model = Serie
        fields = ['nombre', 'rating', 'tags', 'descripcion', 'reseña', 'portada', 'director', 'productoraCinematografica', 'valoracion']


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['nombre']


class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = ['nombre', 'año_debut', 'edad', 'avatar']

class PeliculaResenaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ['reseña']

class SerieResenaForm(forms.ModelForm):
    class Meta:
        model = Serie
        fields = ['reseña']
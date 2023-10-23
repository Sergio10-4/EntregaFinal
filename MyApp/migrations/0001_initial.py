# Generated by Django 4.2.2 on 2023-10-15 11:13

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('año_debut', models.DateField()),
                ('edad', models.IntegerField()),
                ('avatar', models.ImageField(null=True, upload_to='')),
            ],
            options={
                'verbose_name': 'Director',
                'verbose_name_plural': 'Directores De Cine',
                'ordering': ('nombre',),
            },
        ),
        migrations.CreateModel(
            name='Productora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('año_fundacion', models.DateField()),
                ('historia', models.TextField(null=True, validators=[django.core.validators.MaxLengthValidator(250)])),
                ('sede', models.ImageField(null=True, upload_to='')),
            ],
            options={
                'verbose_name': 'Productora',
                'verbose_name_plural': 'Productoras De Cine',
                'ordering': ('nombre',),
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(choices=[('Accion', 'Acción'), ('Comedia', 'Comedia'), ('Drama', 'Drama'), ('Fantasia', 'Fantasía'), ('Animacion', 'Animacion'), ('Terror', 'Terror'), ('Thriller', 'Thriller'), ('Suspenso', 'Suspenso'), ('Sci-Fi', 'Sci-Fi')], max_length=100)),
            ],
            options={
                'verbose_name': 'Generos',
                'verbose_name_plural': 'Generos De Cine',
                'ordering': ('nombre',),
            },
        ),
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('rating', models.IntegerField(null=True)),
                ('descripcion', models.TextField(null=True, validators=[django.core.validators.MaxLengthValidator(250)])),
                ('reseña', models.TextField(null=True, validators=[django.core.validators.MaxLengthValidator(250)])),
                ('portada', models.ImageField(null=True, upload_to='')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.director')),
                ('productoraCinematografica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.productora')),
                ('tags', models.ManyToManyField(to='MyApp.tag')),
            ],
            options={
                'verbose_name': 'Serie',
                'verbose_name_plural': 'Catalogo De Series',
                'ordering': ('nombre',),
            },
        ),
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('rating', models.IntegerField(null=True)),
                ('descripcion', models.TextField(null=True, validators=[django.core.validators.MaxLengthValidator(250)])),
                ('reseña', models.TextField(null=True, validators=[django.core.validators.MaxLengthValidator(250)])),
                ('portada', models.ImageField(null=True, upload_to='')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.director')),
                ('productoraCinematografica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.productora')),
                ('tags', models.ManyToManyField(to='MyApp.tag')),
            ],
            options={
                'verbose_name': 'Pelicula',
                'verbose_name_plural': 'Catalogo De Peliculas',
                'ordering': ('nombre',),
            },
        ),
    ]
# Generated by Django 4.2.2 on 2023-10-16 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelicula',
            name='valoracion',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='serie',
            name='valoracion',
            field=models.URLField(null=True),
        ),
    ]
# Generated by Django 4.2.6 on 2023-11-09 02:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('templatesApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='autor',
            old_name='Apellido',
            new_name='apellidoAutor',
        ),
        migrations.RenameField(
            model_name='autor',
            old_name='FechaNacimiento',
            new_name='fechaNacimiento',
        ),
        migrations.RenameField(
            model_name='autor',
            old_name='id',
            new_name='idAutor',
        ),
        migrations.RenameField(
            model_name='autor',
            old_name='Nombre',
            new_name='nombreAutor',
        ),
        migrations.RenameField(
            model_name='autor',
            old_name='Telefono',
            new_name='telefonoAutor',
        ),
    ]

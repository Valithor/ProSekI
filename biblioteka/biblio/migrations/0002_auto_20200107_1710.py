# Generated by Django 2.2.7 on 2020-01-07 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('biblio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filmrezyser',
            name='idFilm',
        ),
        migrations.RemoveField(
            model_name='filmrezyser',
            name='idRezyser',
        ),
        migrations.RemoveField(
            model_name='filmaktor',
            name='ilosc',
        ),
        migrations.RemoveField(
            model_name='film',
            name='gatunek',
        ),
        migrations.AddField(
            model_name='film',
            name='gatunek',
            field=models.ForeignKey(default='DRAMAT', on_delete=django.db.models.deletion.CASCADE, to='biblio.gatunek'),
        ),
        migrations.RemoveField(
            model_name='film',
            name='rezyser',
        ),
        migrations.AddField(
            model_name='film',
            name='rezyser',
            field=models.ForeignKey(default='STH', on_delete=django.db.models.deletion.CASCADE, to='biblio.rezyser'),
        ),
        migrations.DeleteModel(
            name='filmgatunek',
        ),
        migrations.DeleteModel(
            name='filmrezyser',
        ),
    ]
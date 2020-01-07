# Generated by Django 2.2.7 on 2020-01-07 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('biblio', '0002_auto_20200107_1710'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='gatunek',
        ),
        migrations.RemoveField(
            model_name='film',
            name='rezyser',
        ),
        migrations.CreateModel(
            name='filmrezyser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idFilm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblio.film')),
                ('idRezyser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblio.rezyser')),
            ],
        ),
        migrations.CreateModel(
            name='filmgatunek',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idFilm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblio.film')),
                ('idGatunek', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblio.gatunek')),
            ],
        ),
        migrations.AddField(
            model_name='film',
            name='gatunek',
            field=models.ManyToManyField(through='biblio.filmgatunek', to='biblio.gatunek'),
        ),
        migrations.AddField(
            model_name='film',
            name='rezyser',
            field=models.ManyToManyField(through='biblio.filmrezyser', to='biblio.rezyser'),
        ),
    ]
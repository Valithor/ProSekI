from django.db import models

class gatunek(models.Model):
    idGatunek = models.AutoField(primary_key=True)
    gatunekWybor = [
        ('DRAMAT', 'dramat'),
        ('THRILLER', 'thriller'),
        ('DOKUMENT', 'dokument'),
        ('AKCJA', 'akcja'),
        ('HORROR', 'horror'),
        ('SCIENCE FICTION', 'science fiction'),
        ('ANIMOWANY', 'animowany'),
    ]
    nazwa = models.CharField(max_length=30, choices=gatunekWybor, default='DRAMAT')

class rezyser(models.Model):
    idRezyser = models.AutoField(primary_key=True)
    imie = models.CharField(max_length=25, null=False)
    nazwisko = models.CharField(max_length=25, null=False)
    pochodzenieWybor = [
        ('POLSKA', 'Polska'),
        ('FRANCJA', 'Francja'),
        ('USA', 'Usa'),
        ('NIEMCY', 'Niemcy'),
        ('WIELKA BRYTANIA', 'Wielka Brytania'),
        ('DANIA', 'Dania'),
        ('AZJA', 'Azja'),
        ('INNE', 'Inne'),
    ]
    pochodzenie = models.CharField(max_length=25, choices=pochodzenieWybor, default='POLSKA')
    dataUrodzenia = models.DateField()

class aktor(models.Model):
    idAktor = models.AutoField(primary_key=True)
    imie = models.CharField(max_length=25, null=False)
    nazwisko = models.CharField(max_length=25, null=False)
    pochodzenieWybor = [
    ('POLSKA', 'Polska'),
    ('FRANCJA', 'Francja'),
    ('USA', 'Usa'),
    ('NIEMCY', 'Niemcy'),
    ('WIELKA BRYTANIA', 'Wielka Brytania'),
    ('DANIA', 'Dania'),
    ('AZJA', 'Azja'),
    ('INNE', 'Inne'),
    ]
    pochodzenie = models.CharField(max_length=25, choices=pochodzenieWybor, default='POLSKA')
    dataUrodzenia = models.DateField()

class film(models.Model):
    idFilm = models.AutoField(primary_key=True)
    idRezyser = models.ForeignKey(rezyser)
    idGatunku = models.ForeignKey(gatunek)
    tytul = models.CharField(max_length=25, null=False)
    dataWydania = models.DateField()
    ocenaWybor = [
        ('JEDEN', '1'),
        ('DWA', '2'),
        ('TRZY', '3'),
        ('CZWARTY', '4'),
        ('PIEC', '5'),
        ('CZESC', '6'),
        ('SIEDEM', '7'),
        ('OSIEM', '8'),
        ('DZIEWIEC', '9'),
        ('DZIESIEC', '10'),
        ]
    ocena = models.CharField(max_length=20, choices=ocenaWybor, default='JEDEN')
    fabula = models.CharField(max_length=200)

class filmaktor(models.Model):
    idFilm = models.ForeignKey(film)
    idAktor = models.ForeignKey(aktor)

class filmgatunek(models.Model):
    idFilm = models.ForeignKey(film)
    idGatunek = models.ForeignKey(gatunek)

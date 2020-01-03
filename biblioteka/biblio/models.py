from django.contrib import admin
from django.db import models

class gatunek(models.Model):
    gatunekWybor = [
        ('DRAMAT', 'dramat'),
        ('THRILLER', 'thriller'),
        ('DOKUMENT', 'dokument'),
        ('AKCJA', 'akcja'),
        ('HORROR', 'horror'),
        ('SCIENCE FICTION', 'science fiction'),
        ('ANIMOWANY', 'animowany'),
    ]
    nazwa = models.CharField(max_length=20, choices=gatunekWybor, default='DRAMAT',)

    def __str__(self):
        return '%s' % self.nazwa

class rezyser(models.Model):
    imie = models.CharField(max_length=25)
    nazwisko = models.CharField(max_length=25)
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

    def __str__(self):
        return '%s %s %s %s' % (self.imie, self.nazwisko, self.pochodzenie, self.dataUrodzenia)

class aktor(models.Model):
    imie = models.CharField(max_length=25)
    nazwisko = models.CharField(max_length=25)
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
    def __str__(self):
        return '%s %s %s %s' % (self.imie, self.nazwisko, self.pochodzenie, self.dataUrodzenia)

class film(models.Model):
    tytul = models.CharField(max_length=25)
    rezyser = models.ManyToManyField(rezyser, through="filmrezyser")
    dataWydania = models.DateField()
    gatunek = models.ManyToManyField(gatunek, through='filmgatunek')
    aktor = models.ManyToManyField(aktor, through='filmaktor')
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

    def __str__(self):
        return '%s %s %s %s %s %s %s' % (self.tytul, self.rezyser, self.aktor, self.gatunek, self.dataWydania, self.ocena, self.fabula)

class filmaktor(models.Model):
    idFilm = models.ForeignKey(film, on_delete=models.CASCADE)
    idAktor = models.ForeignKey(aktor, on_delete=models.CASCADE)
    ilosc = models.CharField(max_length=45)

    def __str__(self):
        return "%s %s " % (self.idFilm, self.idAktor)

class filmgatunek(models.Model):
    idFilm = models.ForeignKey(film, on_delete=models.CASCADE)
    idGatunek = models.ForeignKey(gatunek, on_delete=models.CASCADE)
    ilosc = models.CharField(max_length=45)

    def __str__(self):
        return "%s %s" % (self.idFilm, self.idGatunek)

class filmrezyser(models.Model):
    idFilm = models.ForeignKey(film, on_delete=models.CASCADE)
    idRezyser = models.ForeignKey(rezyser, on_delete=models.CASCADE)
    ilosc = models.CharField(max_length=45)

    def __str__(self):
        return "%s %s" % (self.idFilm, self.idRezyser)

class filmaktorInline(admin.TabularInline):
    model = filmaktor
    extra = 1

class filmrezyserInline(admin.TabularInline):
    model = filmaktor
    extra = 1


class filmgatunekInline(admin.TabularInline):
    model = filmgatunek
    extra = 1


class filmAdmin(admin.ModelAdmin):
    inlines = (filmaktorInline, filmgatunekInline, filmrezyserInline,)
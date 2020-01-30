from django.contrib import admin
from django.db import models

class osoba(models.Model):
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
    gatunekWybor = [
        ('DRAMAT', 'dramat'),
        ('THRILLER', 'thriller'),
        ('DOKUMENT', 'dokument'),
        ('AKCJA', 'akcja'),
        ('HORROR', 'horror'),
        ('SCIENCE FICTION', 'science fiction'),
        ('ANIMOWANY', 'animowany'),
    ]
    tytul = models.CharField(max_length=25)
    dataWydania = models.DateField()
    gatunek = models.CharField(max_length=20, choices=gatunekWybor, default='DRAMAT',)
    osoba = models.ManyToManyField(osoba, through='filmosoba')
    fabula = models.CharField(max_length=200)

    def __str__(self):
        return '%s %s %s %s %s' % (self.tytul, self.dataWydania, self.gatunek, self.osoba, self.fabula)
class ocena(models.Model):
    ocenaWybor = [
        ('JEDEN', '1'),
        ('DWA', '2'),
        ('TRZY', '3'),
        ('CZTERY', '4'),
        ('PIEC', '5'),
        ('SZESC', '6'),
        ('SIEDEM', '7'),
        ('OSIEM', '8'),
        ('DZIEWIEC', '9'),
        ('DZIESIEC', '10'),
    ]
    film = models.ForeignKey(film, on_delete=models.CASCADE)
    ocena = models.CharField(max_length=20, choices=ocenaWybor, default='JEDEN')
    recenzja = models.CharField(max_length=200)
    uzytkownik = models.ForeignKey('auth.User', related_name='uzytkownik', blank=True, null=True,
                                         on_delete=models.SET_NULL)
    def __str__(self):
        return '%s %s' % (self.ocena, self.recenzja)

class filmosoba(models.Model):
    osobaWybor = [
        ('aktor', 'AKTOR'),
        ('rezyser', 'REZYSER'),
    ]
    Film = models.ForeignKey(film, on_delete=models.CASCADE)
    Osoba = models.ForeignKey(osoba, on_delete=models.CASCADE)
    rola = models.CharField(max_length=20, choices=osobaWybor, default='AKTOR')


    def __str__(self):
        return "%s %s %s" % (self.Film, self.Osoba, self.rola)

class filmosobaInline(admin.TabularInline):
    model = filmosoba
    extra = 1

class filmAdmin(admin.ModelAdmin):
    inlines = (filmosobaInline, )
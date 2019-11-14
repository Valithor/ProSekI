from django.db import models


class ksiazka(models.Model):
    tytul = models.CharField(max_length=200)
autor = models.CharField(max_length=200)
data_wydania = models.DateField()
dzial = models.CharField(max_length=200)

class uzytkownik(models.Model):
    imie = models.CharField(max_length=200)
    nazwisko = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

class terminy(models.Model):
    ksiazka = models.ForeignKey(ksiazka, on_delete=models.CASCADE)
data_dobioru = models.DateField()
data_oddania = models.DateField()
uzytkownik = models.ForeignKey(uzytkownik, on_delete=models.CASCADE)


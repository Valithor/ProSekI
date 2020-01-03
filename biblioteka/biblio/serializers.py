from .models import film, aktor, gatunek, rezyser, filmgatunek, filmaktor, filmrezyser
from rest_framework import serializers

class aktorSerializer(serializers.ModelSerializer):
    class Meta:
        model = aktor
        fields = ("imie", "nazwisko", "pochodzenie", "dataUrodzenia")

class gatunekSerializer(serializers.ModelSerializer):
    class Meta:
        model = gatunek
        fields = "nazwa"

class rezyserSerializer(serializers.ModelSerializer):
    class Meta:
        model = rezyser
        fields = ("imie", "nazwisko", "pochodzenie", "dataUrodzenia")

class filmaktorSerializer(serializers.ModelSerializer):
    class Meta:
        model = filmaktor
        fields = '__all__'

class filmgatunekSerializer(serializers.ModelSerializer):
    class Meta:
        model = filmgatunek
        fields = '__all__'

class filmrezyserSerializer(serializers.ModelSerializer):
    class Meta:
        model = filmrezyser
        fields = '__all__'

class filmSerializer(serializers.ModelSerializer):
    aktor = filmaktorSerializer(read_only=True, many=True)
    gatunek = filmgatunekSerializer(read_only=True, many=True)
    rezyser = rezyserSerializer(read_only=True, many=False)

    class Meta:
        model = film
        fields = ("tytul", "aktor", "gatunek", "dataWydania", "ocena", "fabula")
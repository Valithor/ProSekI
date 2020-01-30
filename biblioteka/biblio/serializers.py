from .models import film, osoba, filmosoba, ocena
from rest_framework import serializers
from django.contrib.auth.models import User


class osobaSerializer(serializers.ModelSerializer):
    class Meta:
        model = osoba
        fields = ("imie", "nazwisko", "pochodzenie", "dataUrodzenia")

class ocenaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ocena
        fields = '__all__'

class filmosobaSerializer(serializers.ModelSerializer):
    class Meta:
        model = filmosoba
        fields = '__all__'

class filmSerializer(serializers.ModelSerializer):
    osoba = osobaSerializer(read_only=True, many=True)
    class Meta:
        model = film
        fields = ["tytul", "dataWydania", "gatunek", "osoba", "fabula"]

class UzytkownikSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class ocenaGetSerializer(serializers.ModelSerializer):
    film = filmSerializer(read_only=True)
    class Meta:
        model = ocena
        fields = ['id','ocena', 'recenzja', 'film']

class ocenaPostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ocena
        fields = ['ocena', 'recenzja', 'film']

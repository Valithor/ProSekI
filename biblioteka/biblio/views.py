from django.http import HttpResponse
from .models import *
from . import serializers
from rest_framework import generics

def index(request):
    return HttpResponse("Witam w indexie.")

class getAktor(generics.ListAPIView):
    queryset = aktor.objects.all()
    serializer_class = serializers.aktorSerializer

class getGatunek(generics.ListAPIView):
    queryset = gatunek.objects.all()
    serializer_class = serializers.gatunekSerializer

class getRezyser(generics.ListAPIView):
    queryset = rezyser.objects.all()
    serializer_class = serializers.rezyserSerializer

class getFilm(generics.ListAPIView):
    queryset = film.objects.all()
    serializer_class = serializers.filmSerializer

class getFilmaktor(generics.ListAPIView):
    queryset = filmaktor.objects.all()
    serializer_class = serializers.filmaktorSerializer

class getFilmgatunek(generics.ListAPIView):
    queryset = filmgatunek.objects.all()
    serializer_class = serializers.filmgatunekSerializer

class getFilmrezyser(generics.ListAPIView):
    queryset = filmrezyser.objects.all()
    serializer_class = serializers.filmrezyserSerializer
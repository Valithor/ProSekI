from django.http import HttpResponse
from .models import *
from . import serializers
from rest_framework import permissions
from rest_framework import generics
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView



def index(request):
    return HttpResponse("Witam w indexie.")
class Osoba(generics.ListAPIView):
    queryset = osoba.objects.all()
    serializer_class = serializers.osobaSerializer
class osobaRead(generics.ListAPIView):
    serializer_class = serializers.osobaSerializer
    def get_queryset(self):
        pk = self.kwargs['pk']
        return osoba.objects.filter(pk=pk)
class osobaUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = serializers.ocenaSerializer
    queryset = serializers.osobaSerializer
class osobaCreate(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = osoba.objects.all()
    serializer_class = serializers.osobaSerializer
class osobaDelete(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = serializers.osobaSerializer
    def get_queryset(self):
        pk = self.kwargs['pk']
        return osoba.objects.filter(pk=pk)
    def perform_destroy(self, instance):
        pk = self.kwargs['pk']
        Osoba = osoba.objects.get(pk=pk)
        Osoba.delete()

class Film(generics.ListAPIView):
    queryset = film.objects.all()
    serializer_class = serializers.filmSerializer
class filmRead(generics.ListAPIView):
    serializer_class = serializers.filmSerializer
    def get_queryset(self):
        pk = self.kwargs['pk']
        return film.objects.filter(pk=pk)
class filmUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = serializers.ocenaSerializer
    queryset = serializers.filmSerializer
class filmCreate(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = film.objects.all()
    serializer_class = serializers.filmSerializer
class filmDelete(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = serializers.osobaSerializer
    def get_queryset(self):
        pk = self.kwargs['pk']
        return film.objects.filter(pk=pk)
    def perform_destroy(self, instance):
        pk = self.kwargs['pk']
        Film = film.objects.get(pk=pk)
        Film.delete()

class Ocena(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = ocena.objects.all()
    serializer_class = serializers.ocenaSerializer
class ocenaUzytkownik (generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return serializers.ocenaGetSerializer
        else:
            return serializers.ocenaPostUpdateSerializer
    def get_queryset(self):
        user = self.request.user
        return ocena.objects.filter(uzytkownik=user)
    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(uzytkownik=user)
class ocenaUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.ocenaSerializer
    def get_queryset(self):
        user = self.request.user
        return ocena.objects.filter(uzytkownik=user)
    def perform_update(self, serializer):
        user = self.request.user
        serializer.save(uzytkownik=user)
class ocenaDelete(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.ocenaSerializer
    def get_queryset(self):
        user = self.request.user
        return ocena.objects.filter(uzytkownik=user)
    def perform_destroy(self, instance):
        pk = self.kwargs['pk']
        Ocena = ocena.objects.get(pk=pk)
        Ocena.delete()

class Filmosoba(generics.ListAPIView):
    queryset = filmosoba.objects.all()
    serializer_class = serializers.filmosobaSerializer
class FilmosobaCreate(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = filmosoba.objects.all()
    serializer_class = serializers.filmosobaSerializer
class filmosobaUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = serializers.ocenaSerializer
    queryset = serializers.filmSerializer
class filmosobaDelete(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = serializers.osobaSerializer
    def get_queryset(self):
        pk = self.kwargs['pk']
        return filmosoba.objects.filter(pk=pk)
    def perform_destroy(self, instance):
        pk = self.kwargs['pk']
        Filmosoba = filmosoba.objects.get(pk=pk)
        Filmosoba.delete()

class Uzytkownik(generics.ListAPIView):
    serializer_class = serializers.UzytkownikSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(id=user.id)

class Uzytkownicy(generics.ListAPIView):
    serializer_class = serializers.UzytkownikSerializer
    permission_classes = [permissions.IsAdminUser]
    queryset = User.objects.all()


from .models import *
from rest_framework import serializers

class filmSerialzer(serializers.ModelSerializer):
    class Meta:
        model = film
        fields = '__all__'


class aktorSerializer(serializers.ModelSerializer):
    class Meta:
        model = aktor
        fields = '__all__'

class gatunekSerializer(serializers.ModelSerializer):
    class Meta:
        model = gatunek
        fields = '__all__'

class rezyserSerializer(serializers.ModelSerializer):
    class Meta:
        model = rezyser
        fields = '__all__'

class filmaktorSerializer(serializers.ModelSerializer):
    class Meta:
        model = filmaktor
        fields = '__all__'

class filmgatunekSerializer(serializers.ModelSerializer):
    class Meta:
        model = filmgatunek
        fields = '__all__'

class filmSerializer(serializers.ModelSerializer):



from django.db import models

class Song(models.Model):

created = models.DateTimeField(auto_now_add=True)

title = models.CharField(max_length=100, blank=True, null = True, default='')

category = models.TextField()

age = models.IntegerField()

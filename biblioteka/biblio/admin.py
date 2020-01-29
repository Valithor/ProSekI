from django.contrib import admin
from .models import *
admin.site.register(osoba)
admin.site.register(film, filmAdmin)
admin.site.register(ocena)


from django.contrib import admin
from .models import *
admin.site.register(rezyser)
admin.site.register(aktor)
admin.site.register(film, filmAdmin)


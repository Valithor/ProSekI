from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('aktor', views.getAktor.as_view(), name=None),
    path('rezyser', views.getRezyser.as_view(), name=None),
    path('gatunek', views.getGatunek.as_view(), name=None),
    path('film', views.getFilm.as_view(), name=None),
]
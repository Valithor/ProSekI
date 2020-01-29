from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('osoba/', views.Osoba.as_view(), name='osoba'),
    path('osoba/read/<int:pk>/', views.osobaRead.as_view(), name='osobaRead'),
    path('admin/osoba/create/', views.osobaCreate.as_view(), name='ocenaEdit'),
    path('admin/osoba/update/<int:pk>/', views.ocenaUpdate.as_view(), name='ocenaUpdate'),
    path('admin/osoba/delete/<int:pk>/', views.ocenaDelete.as_view(), name='ocenaDelete'),

    path('film/', views.Film.as_view(), name='film'),
    path('film/read/<int:pk>/', views.filmRead.as_view(), name='filmRead'),
    path('admin/film/update/<int:pk>/', views.filmUpdate.as_view(), name='filmUpdate'),
    path('admin/film/create/', views.filmCreate.as_view(), name='filmEdit'),
    path('admin/film/delete/<int:pk>/', views.filmDelete.as_view(), name='filmDelete'),

    path('admin/filmosoba/create/', views.FilmosobaCreate.as_view(), name='filmosobacreate'),
    path('admin/filmosoba/update/<int:pk>/', views.filmosobaUpdate.as_view(), name='filmosobaupdate'),
   # path('admin/filmosoba/delete/<int:pk>/', views.filmosobaDelete.as_view(), name='filmosobadelete'),

    path('admin/ocena/', views.Ocena.as_view(), name='ocena'),
    path('accounts/profile/ocena', views.ocenaUzytkownik.as_view(), name='ocenaUzytkownik'),
    path('accounts/profile/ocena/update/<int:pk>/', views.ocenaUpdate.as_view(), name='ocenaEdit'),
    path('accounts/profile/ocena/delete/<int:pk>/', views.ocenaDelete.as_view(), name='ocenaDelete'),

    path('accounts/profile/', views.Uzytkownik.as_view(), name='Uzytkownik'),
    path('admin/user/', views.Uzytkownicy.as_view(), name='uzytkownicy'),

]
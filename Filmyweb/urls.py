from django.urls import path
from Filmyweb.views import wszystkie_filmy, nowy_film, \
    edytuj_film, usun_film, details_film, ocen_film, dodaj_aktora

urlpatterns = [
    path('wszystkie/', wszystkie_filmy, name='wszystkie_filmy'),
    path('nowy/', nowy_film, name='nowy_film'),
    path('edytuj/<int:id>/', edytuj_film, name='edytuj_film'),
    path('usun/<int:id>/', usun_film, name='usun_film'),
    path('details/<int:id>/', details_film, name='details_film'),
    path('ocen/<int:id>/', ocen_film, name='ocen_film'),
    path('aktor/<int:id>/', dodaj_aktora, name='dodaj_aktora'),

]
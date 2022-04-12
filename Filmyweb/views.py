from django.shortcuts import render, get_object_or_404, redirect
from .models import Film, DodatkoweInfo, Ocena
from .forms import FilmForm, DodatkoweInfoForm, OcenaForm, AktorForm
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer, FilmSerializer

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class FilmView(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

def wszystkie_filmy(request):
    wszystkie = Film.objects.all()
    return render(request, 'filmy.html', {'filmy': wszystkie})


def details_film(request, id):
    film = get_object_or_404(Film, pk=id)
    oceny = Ocena.objects.filter(film=film)
    aktorzy = film.aktorzy.all()

    if request.method == "POST":
        film.objects.filter(id)

    return render(request, 'details.html', {'film': film, 'oceny': oceny, 'aktorzy': aktorzy})

@login_required()
def nowy_film(request):
    form_film = FilmForm(request.POST or None, request.FILES or None)
    form_dodatkowe = DodatkoweInfoForm(request.POST or None)

    if all((form_film.is_valid(), form_dodatkowe.is_valid())):
        film = form_film.save(commit=False)
        dodatkowe = form_dodatkowe.save()
        film.dodatkowe = dodatkowe
        film.save()
        return redirect(wszystkie_filmy)

    return render(request, 'film_form.html', {'form': form_film, 'form_dodatkowe': form_dodatkowe, 'nowy': True})

@login_required()
def edytuj_film(request, id):
    film = get_object_or_404(Film, pk=id)


    try:
        dodatkowe = DodatkoweInfo.objects.get(film=film.id)
    except DodatkoweInfo.DoesNotExist:
        dodatkowe = None

    form_film = FilmForm(request.POST or None, request.FILES or None, instance=film)
    form_dodatkowe = DodatkoweInfoForm(request.POST or None, instance=dodatkowe)


    if all((form_film.is_valid(), form_dodatkowe.is_valid())):
        film = form_film.save(commit=False)
        dodatkowe = form_dodatkowe.save()
        film.dodatkowe = dodatkowe
        film.save()
        return redirect(wszystkie_filmy)

    return render(request, 'film_form.html', {'form': form_film, 'form_dodatkowe': form_dodatkowe, 'nowy': False})

@login_required()
def usun_film(request, id):
    film = get_object_or_404(Film, pk=id)

    if request.method == "POST":
        film.delete()
        return redirect(wszystkie_filmy)

    return render(request, 'potwierdz.html', {'film': film})

@login_required()
def ocen_film(request, id):
    film = get_object_or_404(Film, pk=id)
    oceny = Ocena.objects.filter(film=film)

    form_ocena = OcenaForm(request.POST or None)

    if request.method == 'POST':
        if 'gwiazdki' in request.POST:
            ocena = form_ocena.save(commit=False)
            ocena.film = film
            ocena.save()
            return redirect(wszystkie_filmy)

    return render(request, 'ocen.html', {'oceny': oceny, 'form_ocena': form_ocena})

@login_required()
def dodaj_aktora(request, id):
    film = get_object_or_404(Film, pk=id)
    aktorzy = film.aktorzy.all()

    form_aktor = AktorForm(request.POST or None)

    if request.method == 'POST':
        if 'imie' in request.POST:
            aktor = form_aktor.save(commit=False)
            aktor.film = film
            aktor.save()

    return render(request, 'aktor.html', {'aktorzy': aktorzy, 'form_aktor': form_aktor})
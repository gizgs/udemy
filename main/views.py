from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Movie
from .forms import MovieForm


# Create your views here.


@login_required
def wszystkie_filmy(request):
    user1 = request.user.id
    if user1 == 1:
        filmy = Movie.objects.all()
        user = request.user
        return render(request, 'lista_filmow.html', {'filmy':filmy, 'user': user})
    else:
        filmy = Movie.objects.filter(id_user=request.user)
        user = request.user
        return render(request, 'lista_filmow.html', {'filmy':filmy, 'user': user})
@login_required
def nowy_film(request):
    form = MovieForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        film = form.save(commit=False)
        film.id_user = request.user
        form.save()
        return redirect(wszystkie_filmy)

    return render(request, 'nowy_film.html', {'form':form})

@login_required
def edytuj_film(request, id):
    film = get_object_or_404(Movie, pk=id)
    form = MovieForm(request.POST or None, request.FILES or None, instance=film)
    if form.is_valid():
        film = form.save(commit=False)
        film.id_user = request.user
        form.save()
        return redirect(wszystkie_filmy)
    return render(request, 'nowy_film.html', {'form':form})

@login_required
def usun_film(request, id):
    film = get_object_or_404(Movie, pk=id)

    if request.method == 'POST':
        film.delete()
        return redirect(wszystkie_filmy)
    return render(request, 'potwierdz.html', {'film': film})

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Movie
from .forms import MovieForm


# Create your views here.
def wszystkie_filmy(request):
    filmy = Movie.objects.all()
    return render(request, 'lista_filmow.html', {'filmy':filmy})

def nowy_film(request):
    form = MovieForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect(wszystkie_filmy)

    return render(request, 'nowy_film.html', {'form':form})

from django.urls import path
from .views import wszystkie_filmy
from .views import nowy_film, edytuj_film, usun_film

urlpatterns = [
    path('new/', nowy_film, name = 'nowy_film'),
    path('edit/<int:id>/', edytuj_film, name = 'edytuj_film'),
    path('delete/<int:id>/', usun_film, name = 'usun_film'),

]

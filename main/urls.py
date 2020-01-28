from django.urls import path
from .views import wszystkie_filmy
from .views import nowy_film

urlpatterns = [
    path('filmy/', wszystkie_filmy),
    path('new/', nowy_film),


]

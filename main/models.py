from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):

    name = models.CharField("Nazwa filmu", max_length=128)
    description = models.TextField(default="")
    year = models.IntegerField(null=True, blank=True)
    released = models.DateField(null=True, blank=True)
    imdb_rating = models.DecimalField(null=True, blank=True, decimal_places=7, max_digits=10)
    photo = models.ImageField(null=True, blank=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_with_year()

    def name_with_year(self):
        return str(self.name) + " (" + str(self.year) + ")"

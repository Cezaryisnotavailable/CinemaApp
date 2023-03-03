from django.db import models
from project_cinema.models import Movie
# Create your models here.


class Cinema(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    movies = models.ManyToManyField(Movie, through="Screening")


class Screening(models.Model):
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    date = models.DateTimeField()



from rest_framework import generics

from project_cinema.models import Movie
from project_cinema.serializers import MovieSerializer


# Create your views here.


class MovieListView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

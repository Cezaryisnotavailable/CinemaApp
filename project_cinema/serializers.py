from rest_framework import serializers

from project_cinema.models import Person, Movie


class MovieSerializer(serializers.ModelSerializer):
    actors = serializers.SlugRelatedField(many=True, slug_field="name", queryset=Person.objects.all())
    directors = serializers.SlugRelatedField(slug_field="name", queryset=Person.objects.all())

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "director", "year", "actors")
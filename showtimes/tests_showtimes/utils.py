from random import sample

import pytz
from faker import Faker
from faker.providers import DynamicProvider

from CinemaApi.settings import TIME_ZONE
from project_cinema.models import Movie
from showtimes.models import Screening, Cinema


cinemas_names_provider = DynamicProvider(
    provider_name="cinemas_names",
    elements=["Kino Moskwa", "Kino 5D", "Kino Bajka", "Kino Aurora", "Kino Pionier", "Kino Wolność", "Kino Corso",
              "Kino Studenckie", "Kino Zew", "Kino Bioskop"]
)
faker = Faker("pl_PL")
faker.add_provider(cinemas_names_provider)
TZ = pytz.timezone(TIME_ZONE)


def random_movies():
    """Return 3 random Movies from db"""
    movies = list(Movie.objects.all())
    return sample(movies, 3)


def add_screening(cinema):
    """Add 3 screenings for a given cinema"""
    movies = random_movies()
    for movie in movies:
        Screening.objects.create(cinema=cinema, movie=movie, date=faker.date_time(tzinfo=TZ))


def fake_cinema_data():
    """Generate fake data for cinema"""
    return {
        # "name": faker.cinemas_names(),
        "name": faker.name(),
        "city": faker.city(),
    }


def create_fake_cinema():
    """Create fake cinema with some screenings"""
    cinema = Cinema.objects.create(**fake_cinema_data())
    add_screening(cinema)

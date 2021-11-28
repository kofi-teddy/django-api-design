from django.shortcuts import render
from django.http import HttpResponse

from .models import Movie, Movie


def movie_list(request):
    movies = Movie.objects.all()
    data = {
        'movies': list(movies.values()),
    }
    return JsonResponse(data)

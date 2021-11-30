from django.http import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import render
import json


from .models import Movie


def movie_list(request):
    movies = Movie.objects.all()
    data = {'movies': list(movies.values())}
    return JsonResponse(data)

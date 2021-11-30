from django.urls import path

# from apps.watchlist.api.views import movie_list, movie_detail
from apps.watchlist.api.views import MovieList, MovieDetail

urlpatterns = [
    path('list/', MovieList.as_view(), name='movie-list'),
    path('<int:pk>/', MovieDetail.as_view(), name='movie-detail'),
]

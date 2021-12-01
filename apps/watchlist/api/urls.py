from django.urls import path

# from apps.watchlist.api.views import movie_list, movie_detail
from apps.watchlist.api.views import WatchList, WatchDetail

urlpatterns = [
    path('list/', WatchList.as_view(), name='movie-list'),
    path('<int:pk>/', WatchDetail.as_view(), name='movie-detail'),
]

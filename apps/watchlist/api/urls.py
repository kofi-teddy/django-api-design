from django.urls import path

from apps.watchlist.api.views import WatchList, WatchDetail, StreamPlatform

urlpatterns = [
    path('list/', WatchList.as_view(), name='movie-list'),
    path('<int:pk>/', WatchDetail.as_view(), name='movie-detail'),
    path('stream/', StreamPlatform.as_view(), name='stream'),
]

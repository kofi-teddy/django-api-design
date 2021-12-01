from django.urls import path

from apps.watchlist.api.views import WatchListAV, WatchDetailAV, StreamPlatformAV, StreamPlatformDetailAV, ReviewList, ReviewDetail

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='movie-detail'),
    path('stream/', StreamPlatformAV.as_view(), name='stream'),
    path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),
    
    path('stream/<int:pk>/review/', StreamPlatformDetailAV.as_view(), name='streamplatformreview-list'),
    path('stream/review/<int:pk>/', ReviewDetail.as_view(), name='review-detail')
]

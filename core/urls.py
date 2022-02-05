from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('watch/', include('apps.watchlist.api.urls')),
    path('', include('puppies.urls')),
    path('api-auth/', namespace='rest_framework'),
]

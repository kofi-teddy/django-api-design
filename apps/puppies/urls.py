from django.urls import path

from apps.puppies import views

urlpatterns = [
    path('api/v1/puppies/<pk>/', views.get_delete_update_puppy, name='get_delete_update_puppy'),
    path('api/v1/puppies/', views.get_post_puppies, name='get_post_puppies'),
]

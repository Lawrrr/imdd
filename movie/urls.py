from django.urls import path

from .views import movie

urlpatterns = [
    path('movies', movie.get_all),
    path('movie/<int:id>', movie.get),
    path('movie/<int:id>/delete', movie.delete),
    path('movie/create', movie.create)
]

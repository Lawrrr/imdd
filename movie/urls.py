from django.urls import path

from .views import movie

urlpatterns = [
    path('movies', movie.get_all),
    path('movie/create', movie.create),
    path('movie/<int:id>', movie.get),
    path('movie/<int:id>/update', movie.update),
    path('movie/<int:id>/delete', movie.delete)
]

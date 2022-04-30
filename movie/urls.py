from django.urls import path

from .views import movie, director

urlpatterns = [
    path('movies', movie.get_all),
    path('movie/create', movie.create),
    path('movie/<int:id>', movie.get),
    path('movie/<int:id>/update', movie.update),
    path('movie/<int:id>/delete', movie.delete),

    path('directors', director.get_all)
]

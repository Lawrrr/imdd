from django.urls import path

from . import views

urlpatterns = [
    path('movies', views.get_all_movies)
]

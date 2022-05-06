from django.urls import path
from rest_framework import routers

from .views import movie, director

router = routers.SimpleRouter()
router.register(r'directors', director.DirectorViewset, basename='directors')

urls = [
    path('movies/', movie.get_all),
    path('movie/create', movie.create),
    path('movie/<int:id>', movie.get),
    path('movie/<int:id>/update', movie.update),
    path('movie/<int:id>/delete', movie.delete)
]

# Urls for Viewset
urlpatterns = urls + router.urls

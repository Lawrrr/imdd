import site
from django.contrib import admin
from movie.models import Movie, Director, Genre

admin.site.register(Movie)
admin.site.register(Director)
admin.site.register(Genre)

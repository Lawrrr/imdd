from django.db import models


class Genre(models.Model):
    genre = models.CharField(max_length=200, null=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.genre

    class Meta:
        ordering = ['genre']


class Director(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    date_of_birth = models.DateField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (self.first_name + " " + self.last_name)


class Movie(models.Model):
    title = models.CharField(max_length=200, null=False)
    genre = models.ManyToManyField(Genre)
    director = models.ForeignKey(
        Director, on_delete=models.CASCADE, null=False)
    release_date = models.DateField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['release_date']

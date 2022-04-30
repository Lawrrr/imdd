from rest_framework import serializers
from .models import Movie, Director


class MovieSerializer(serializers.ModelSerializer):
    genre = serializers.StringRelatedField(many=True, read_only=True)
    director = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'director',
                  'release_date', 'created_on', 'updated_on']


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['id', 'first_name', 'last_name',
                  'date_of_birth', 'created_on', 'updated_on']

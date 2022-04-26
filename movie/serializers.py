from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    genre = serializers.StringRelatedField(many=True, read_only=True)
    director = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Movie
        fields = ['title', 'genre', 'director',
                  'release_date', 'created_on', 'updated_on']

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import Movie
from ..serializers import MovieSerializer


@api_view(['GET'])
def get_all(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def get(request, **kwargs):
    if request.method == 'GET':
        try:
            movie = Movie.objects.get(id=kwargs['id'])
            serializer = MovieSerializer(movie)
            return Response(serializer.data)
        except:
            data = {
                "status": "error",
                "message": "Movie doesn't exist..."
            }
            return Response(data, status=status.HTTP_404_NOT_FOUND)

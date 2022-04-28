from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import Movie, Director
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
                'status': 'error',
                'message': 'Movie doesn\'t exist...'
            }

            return Response(data, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def create(request):
    if request.method == 'POST':
        movie = request.data
        try:
            checkMovie = Movie.objects.filter(title=movie['title']).exists()

            if not checkMovie:
                getDirector = Director.objects.get(id=movie['director'])

                newMovie = Movie.objects.create(
                    title=movie['title'],
                    director=getDirector,
                    release_date=movie['release_date']
                )
                
                # Add genre/s to newly created movie
                for genre in movie['genre']:
                    newMovie.genre.add(genre)
                    
                movieSerialize = MovieSerializer(newMovie)
                data = {
                    'status': 'success',
                    'message': 'New movie added!',
                    'movie': movieSerialize.data
                }

                return Response(data)
            else:
                data = {
                    'status': 'error',
                    'message': 'Movie already in the database.'
                }

                return Response(data, status=status.HTTP_409_CONFLICT)

        except:
            data = {
                'status': 'error',
                'message': 'Movie not created.'
            }

            return Response(data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete(request, **kwargs):
    try:
        Movie.objects.get(id=kwargs['id']).delete()

        data = {
            'status': 'success',
            'message': 'Movie successfully deleted!'
        }
    
        return Response(data)
    except:
        data = {
            'status': 'error',
            'message': 'Failed to delete movie.'
        }
        
        return Response(data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update(request, **kwargs):
    try:
        updateData = request.data
        movie = Movie.objects.get(id=kwargs['id'])
        for key, value in updateData.items():
            # For foreign keys(director & genre) I could create a different function.
            if key == 'director':
                getDirector = Director.objects.get(id=value)
                movie.director = getDirector
            elif key == 'genre':
                movie.genre.set(value)
            elif value:
                setattr(movie, key, value)
            else:
                raise

        movie.save()
        serializeMovie = MovieSerializer(movie)
        data = {
            'status': 'success',
            'message': 'Movie successfully updated',
            'movie': serializeMovie.data
        }

        return Response(data)
    except:
        data = {
            'status': 'error',
            'message': 'Movie update failed'
        }

    return Response(data, status=status.HTTP_400_BAD_REQUEST)

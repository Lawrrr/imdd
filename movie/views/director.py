from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from ..models import Director
from ..serializers import DirectorSerializer


class DirectorViewset(viewsets.ViewSet):
    """
    CRUD Directors
    """

    def list(self, request):
        directors = Director.objects.all()
        serializer = DirectorSerializer(directors, many=True)

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        directors = Director.objects.all()
        director = get_object_or_404(directors, pk=pk)
        serializer = DirectorSerializer(director)

        return Response(serializer.data)

    def create(self, request):
        inputData = request.data

        director = Director.objects.create(
            first_name=inputData['first_name'],
            last_name=inputData['last_name'],
            date_of_birth=inputData['date_of_birth']
        )
        serializer = DirectorSerializer(director)

        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            updateData = request.data
            directors = Director.objects.all()
            director = get_object_or_404(directors, pk=pk)

            for key, value in updateData.items():
                setattr(director, key, value)

            director.save()
            serializer = DirectorSerializer(director)

            return Response(serializer.data)
        except:
            data = {
                'status': 'error',
                'message': 'Update unsuccessful.'
            }
        
        return Response(data, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            Director.objects.get(id=pk).delete()

            data = {
                'status': 'success',
                'message': 'Director successfully deleted.'
            }

            return Response(data)
        except:
            data = {
                'status': 'error',
                'message': 'Deletion unsuccessful'
            }

            return Response(data, status=status.HTTP_404_NOT_FOUND)

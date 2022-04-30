from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Director
from ..serializers import DirectorSerializer


@api_view(['GET'])
def get_all(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        serializer = DirectorSerializer(directors, many=True)

        return Response(serializer.data)

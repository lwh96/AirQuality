from rest_framework import viewsets
from rest_framework.response import Response
from .city import cities
from .serializer import CitySerializer


class CityViewSet(viewsets.ViewSet):
    serializer_class = CitySerializer

    def list(self, request):
        serializer = CitySerializer(
            instance=cities.values(), many=True)
        return Response(serializer.data)
from rest_framework import serializers


class CitySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    csvname = serializers.CharField(max_length=256)

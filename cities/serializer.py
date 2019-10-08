from rest_framework import serializers
from .city import City


class CitySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    csvname = serializers.CharField(max_length=256)

    def create(self, validated_data):
        return City(id=None, **validated_data)

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        return instance

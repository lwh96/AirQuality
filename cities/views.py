from rest_framework import viewsets
from rest_framework.response import Response
import pandas as pd

from .city import cities
from .serializer import CitySerializer


class CityViewSet(viewsets.ViewSet):
    serializer_class = CitySerializer

    def list(self, request):
        serializer = CitySerializer(
            instance=cities.values(), many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        print(cities)
        serializer = CitySerializer(instance=cities[pk], many=False)
        return Response(serializer.data)

    # Util Functions
    def calc_std_dev(self, filename):
        df = pd.read_csv(filename)

        measures = ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']

        data = {}

        for measure in measures:
            dfgt20 = df.dropna(subset=[measure, 'TEMP'], how='any').query('TEMP > 20')
            dflte20 = df.dropna(subset=[measure, 'TEMP'], how='any').query('TEMP <= 20')
            data[measure] = {}
            data[measure]['Above 20'] = dfgt20[measure].std()
            data[measure]['20 and Below'] = dflte20[measure].std()

        return data

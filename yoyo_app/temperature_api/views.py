import os

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from yoyo_app.temperature_api.helpers import WeatherApiCall
from yoyo_app.temperature_api.serializers import TemperatureSerializer

WEATHER_API_KEY = os.getenv(
    "WEATHER_API_KEY", default="")


class TemperatureView(APIView):

    permission_classes = (AllowAny,)
    serializer_class = TemperatureSerializer

    def get(self, request, city: str, format=None):
        days = request.GET.get('days')
        payload = dict({
            'city': city,
            'days': days
        })
        serializer = self.serializer_class(data=payload)
        serializer.is_valid(raise_exception=True)
        api_call_obj = WeatherApiCall(days, city)
        data = api_call_obj.get_weather_stats()
        return Response(data, status=status.HTTP_200_OK)

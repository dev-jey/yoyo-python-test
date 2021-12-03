"""Logic for the temperature api module."""
import os

from drf_yasg2 import openapi
from drf_yasg2.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import action
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
    # Include URL param in swagger documentation
    url_param = openapi.Parameter(
        'days', openapi.IN_QUERY,
        description="number of days to obtain forecast",
        type=openapi.TYPE_INTEGER,
        required=True)

    @swagger_auto_schema(method='get',
                         manual_parameters=[url_param])
    @action(methods=['GET'], detail=True)
    def get(self, request: object, city: str, format=None):
        """
        Get minimum, maximum, average and median temperatures
        Args:
            request: (obj) request object
            city: (str) name of a city
            format: (optional)
        Returns:
            data: (obj) contains the maximum, minimum, median, and average
                    temperatures
        """
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

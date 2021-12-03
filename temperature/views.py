import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from temperature.serializers import TemperatureSerializer

WEATHER_API_KEY = os.getenv(
    "WEATHER_API_KEY", "f631ca2cd6394b7283984138210312")


class TemperatureView(APIView):
    """
    """

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
        breakpoint()
        return Response(serializer.data, status=status.HTTP_200_OK)

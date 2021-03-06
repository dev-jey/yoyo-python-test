import logging
import os
from statistics import median
from typing import Dict, List

import requests
from rest_framework.serializers import ValidationError

logger = logging.getLogger(__name__)


class WeatherApiCall(object):
    """
        Class initializes and object to make api calls to weather api
        Args:
            days: (str) number of days to forecast.
            city: (str) name of a city.
        Returns:
            data: (obj) contains the maximum, minimum, median, and average
                    temperatures.
    """

    def __init__(self, days: int, city: str) -> None:
        """Initialize all variables for an object."""
        self.WEATHER_API_KEY = os.getenv(
            "WEATHER_API_KEY", "")
        self.base_api_url = "http://api.weatherapi.com/v1/"
        self.days = days
        self.city = city

    def get_weather_stats(self) -> Dict:
        """Make API call to the weather API."""
        formatted_stats = dict()
        API_URL = f"""{self.base_api_url}forecast.json?
                    days={self.days}&key=
                    {self.WEATHER_API_KEY}&q={self.city}"""
        api_response = requests.get(API_URL)
        if api_response.status_code != 200:
            raise ValidationError({
                "error":
                api_response.json().get("error").get("message", "")
            })
        forecasts = api_response.json().get(
            "forecast", dict()).get("forecastday", [])
        if forecasts:
            formatted_stats = self.calculate_temperature_values(forecasts)
        return formatted_stats

    def calculate_temperature_values(self, forecasts: List) -> Dict:
        """Calculate the response values from the API output. """
        hourly_temps = [temp.get("temp_c") for value in forecasts
                        for temp in value.get("hour")]
        max_temp = max(hourly_temps)
        min_temp = min(hourly_temps)
        avg_temp = sum(hourly_temps) / len(hourly_temps)
        median_temp = median(hourly_temps)
        return dict({
            "maximum": max_temp,
            "minimum": min_temp,
            "average": round(avg_temp, 2),
            "median": median_temp
        })

import os
from statistics import median
from typing import Dict, List

import requests


class WeatherApiCall(object):
    def __init__(self, days: int, city: str) -> None:
        self.WEATHER_API_KEY = os.getenv(
            "WEATHER_API_KEY", "f631ca2cd6394b7283984138210312")
        self.base_api_url = "http://api.weatherapi.com/v1/"
        self.days = days
        self.city = city

    def get_weather_stats(self) -> Dict:
        formatted_stats = dict()
        API_URL = f"""{self.base_api_url}forecast.json?
                    days={self.days}&key=
                    {self.WEATHER_API_KEY}&q={self.city}"""
        api_response = requests.get(API_URL)
        forecasts = api_response.json().get(
            "forecast", dict()).get("forecastday", [])
        if forecasts:
            formatted_stats = self.calculate_temperature_values(forecasts)
        return formatted_stats

    def calculate_temperature_values(self, forecasts: List) -> Dict:
        max_temp = max(forecasts, key=lambda item: item["day"]["maxtemp_c"])
        min_temp = min(forecasts, key=lambda item: item["day"]["mintemp_c"])
        hourly_temps = [temp.get("temp_c") for value in forecasts
                        for temp in value.get("hour")]
        avg_temp = sum(hourly_temps) / len(hourly_temps)
        median_temp = median(hourly_temps)
        return dict({
            "maximum": max_temp["day"]["maxtemp_c"],
            "minimum": min_temp["day"]["maxtemp_c"],
            "average": round(avg_temp, 2),
            "median": median_temp
        })

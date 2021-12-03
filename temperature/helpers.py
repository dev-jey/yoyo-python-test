import os
from typing import Dict, List
import requests


class WeatherApiCall(object):
    def __init__(self, days: int, city: str) -> None:
        self.WEATHER_API_KEY = os.getenv(
            "WEATHER_API_KEY", "f631ca2cd6394b7283984138210312")
        self.days = days
        self.city = city

    def get_weather_stats() -> List[Dict]:
        API_URL = f"http://api.weatherapi.com/v1/forecast.json?days={days}&key={WEATHER_API_KEY}&q={city}"
        api_response = requests.get(API_URL)
        forecasts = api_response.json().get("forecast").get("forecastday")
        return forecasts

    def format_response_data(forecasts: List) -> List[Dict]:
        temperature_list = []
        for forecast in forecasts:
            temp_data = forecast.get("day")
            temperature_list.append({
                "date": forecast.get('date'),
                "maximum": temp_data.get("maxtemp_c"),
                "minimum": temp_data.get("mintemp_c"),
                "average": temp_data.get("avgtemp_c"),
                "median": 12
            })
        return temperature_list

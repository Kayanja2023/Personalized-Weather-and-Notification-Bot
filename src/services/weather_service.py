import requests
import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)

class WeatherService:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, location: str) -> Dict[str, Any]:
        """
        Fetch weather data for a given location
        """
        try:
            params = {
                'q': location,
                'appid': self.api_key,
                'units': 'metric'
            }
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logger.error(f"Error fetching weather data: {str(e)}")
            raise

    def format_weather_message(self, weather_data: Dict[str, Any]) -> str:
        """
        Format weather data into a readable message
        """
        try:
            temp = weather_data['main']['temp']
            description = weather_data['weather'][0]['description']
            humidity = weather_data['main']['humidity']
            
            return (f"Current weather: {description}\n"
                   f"Temperature: {temp}°C\n"
                   f"Humidity: {humidity}%")
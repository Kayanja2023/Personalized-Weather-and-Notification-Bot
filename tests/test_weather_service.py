import unittest
from unittest.mock import patch, MagicMock
from src.services.weather_service import WeatherService

class TestWeatherService(unittest.TestCase):
    def setUp(self):
        self.weather_service = WeatherService("test_api_key")

    @patch('requests.get')
    def test_get_weather(self, mock_get):
        # Mock response
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "main": {"temp": 20, "humidity": 65},
            "weather": [{"description": "clear sky"}]
        }
        mock_get.return_value = mock_response

        # Test weather data retrieval
        result = self.weather_service.get_weather("London")
        self.assertEqual(result["main"]["temp"], 20)
        self.assertEqual(result["main"]["humidity"], 65)
        self.assertEqual(result["weather"][0]["description"], "clear sky")
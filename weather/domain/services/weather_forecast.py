import datetime
from dataclasses import dataclass
from typing import List

import requests

from weather.domain.entities import DayForecast


@dataclass
class WeatherForecastService:
    base_url: str
    api_key: str

    def get_weather_forecasts(self, lat: float, lng: float) -> List[DayForecast]:
        endpoint = f'{self.base_url}/onecall?lat={lat}&lon={lng}&exclude=current,minutely,hourly&appid={self.api_key}&lang=es'
        headers = {
            'Content-Type': 'application/json',
        }
        response = requests.get(endpoint, headers=headers)
        if response.status_code not in [200, 201]:
            raise Exception(f'Error getting weather day forecasts lat={lat} lon={lng}')
        response_json = response.json()
        daily_forecasts = response_json.get('daily', [])
        return [
            DayForecast(
                day=self.epoch_to_date(forecast.get('dt')),
                max=forecast.get('temp', {}).get('max'),
                min=forecast.get('temp', {}).get('min'),
                weather=forecast.get('weather', [{}])[0].get('main'),
            )
            for forecast in daily_forecasts
        ]

    @staticmethod
    def epoch_to_date(epoch: int) -> datetime.date:
        return datetime.datetime.fromtimestamp(epoch).date()
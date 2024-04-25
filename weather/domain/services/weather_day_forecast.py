
from concurrent.futures import ThreadPoolExecutor, wait
from dataclasses import dataclass
from typing import List, Optional, Set

from weather.domain.entities import CityWeatherDayForecast, City
from weather.domain.services.city import CityService
from weather.domain.services.weather_forecast import WeatherForecastService


@dataclass
class WeatherDayForecast:
    city_to_search: str
    city_service: CityService
    weather_forecast_service: WeatherForecastService

    def execute(self) -> List[CityWeatherDayForecast]:
        cities = self.city_service.get_cities(city=self.city_to_search)
        return self._parallel_executor(cities=cities, num_task=len(cities))

    def _parallel_executor(self, cities: List[City], num_task: Optional[int] = None) -> List[CityWeatherDayForecast]:
        city_weather_days = []
        with ThreadPoolExecutor(max_workers=num_task) as executor:
            responses = [
                executor.submit(self._get_weather_day_forecast, city) for city in cities
            ]
            wait(responses)
            for response in responses:
                city_weather_days.append(response.result())
        return city_weather_days

    def _get_weather_day_forecast(self, city: City) -> CityWeatherDayForecast:
        return CityWeatherDayForecast(
            city=city,
            weather_forecast=self.weather_forecast_service.get_weather_forecasts(
                lat=city.lat,
                lng=city.lng,
            ),
        )

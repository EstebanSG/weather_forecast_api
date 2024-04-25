from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from typing import List


@dataclass
class City(object):
    id: str
    name: str
    lat: float
    lng: float


@dataclass
class DayForecast(object):
    day: date
    max: Decimal
    min: Decimal
    weather: str


@dataclass
class CityWeatherDayForecast(object):
    city: City
    weather_forecast: List[DayForecast]

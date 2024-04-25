from django.shortcuts import render
from weather.domain.services.city import CityService
from weather.domain.services.weather_day_forecast import WeatherDayForecast
from weather.domain.services.weather_forecast import WeatherForecastService
from weather_forecast_api.settings import (
    RESERVAMOS_BASE_URL,
    OPEN_WEATHER_BASE_URL,
    OPEN_WEATHER_API_KEY,
)


def index(request):
    return render(request, 'weather/index.html')


def search(request):
    print('request: ', request.GET)
    if not request.GET.get('city'):
        return render(
            request,
            "weather/index.html",
            {
                "error_message": "You didn't entry a city.",
            },
        )
    else:
        weather_day_forecast = WeatherDayForecast(
            city_to_search=request.GET['city'],
            city_service=CityService(
                base_url=RESERVAMOS_BASE_URL,
            ),
            weather_forecast_service=WeatherForecastService(
                base_url=OPEN_WEATHER_BASE_URL,
                api_key=OPEN_WEATHER_API_KEY,
            ),
        )
        cities_weather = weather_day_forecast.execute()
        return render(request, "weather/results.html", {
            'search': request.GET['city'],
            'cities': cities_weather,

        })

from dataclasses import dataclass
from typing import List
import requests
from weather.domain.entities import City


@dataclass
class CityService:
    base_url: str
    valid_place_type: str = 'city'

    def get_cities(self, city: str) -> List[City]:
        endpoint = f'{self.base_url}places?q={city}'
        headers = {
            'Content-Type': 'application/json',
        }
        response = requests.get(endpoint, headers=headers)
        if response.status_code not in [200, 201]:
            raise Exception('Error getting cities')
        return self._validate_city(response.json())

    def _validate_city(self, response_json: list[dict]):
        city_list = []
        for place in response_json:
            if not place.get('long') and not place.get('lat') and place.get('result_type') != self.valid_place_type:
                continue
            city_list.append(
                City(
                    id=place.get('id'),
                    name=place.get('city_name'),
                    lat=round(float(place.get('lat')), 4),
                    lng=round(float(place.get('long')), 4),
                )
            )
        return city_list

from dataclasses import dataclass
from typing import List

import requests


@dataclass
class Place(object):
    id: str
    city_name: str
    state: str
    country: str
    lat: float
    lng: float


@dataclass
class HttpPlaceService():
    # base_url: str

    def get_places(self, place: str) -> List[Place]:
        endpoint = f'https://search.reservamos.mx/api/v2/places?q={place}'
        headers = {
            'Content-Type': 'application/json',
        }
        response = requests.get(endpoint, headers=headers)
        if response.status_code not in [200, 201]:
            raise Exception('Error getting places')
        response_json = response.json()
        return [
            Place(
                id=place.get('id'),
                city_name=place.get('city_name'),
                state=place.get('state'),
                country=place.get('country'),
                lat=float(place.get('lat')),
                lng=float(place.get('long')),
            )
            for place in response_json if place.get('lat') and place.get('long')
        ]

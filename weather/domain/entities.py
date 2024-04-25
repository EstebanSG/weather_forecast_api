from dataclasses import dataclass
from typing import List

import requests


@dataclass
class City(object):
    id: str
    name: str
    lat: float
    lng: float
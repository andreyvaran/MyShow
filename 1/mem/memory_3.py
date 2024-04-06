import random
from dataclasses import dataclass

from pydantic import BaseModel
from pympler import asizeof
from collections import *

@dataclass(slots=True)
class GeoPoint:
    latitude: float
    longitude: float
    elevation: float


points = [GeoPoint(latitude=random.random(), longitude=random.random(), elevation=random.random()) for _ in
          range(100000)]


class RegularPoint:
    def __init__(self, latitude: float, longitude: float, elevation: float):
        self.latitude = latitude
        self.longitude = longitude
        self.elevation = elevation


new_points = [RegularPoint(latitude=random.random(), longitude=random.random(), elevation=random.random()) for _ in
              range(100000)]



class GeoPointPydantic(BaseModel):
    latitude: float
    longitude: float
    elevation: float
    # class Config:
    #     slots = True

pydantic_points = [GeoPointPydantic(latitude=random.random(), longitude=random.random(), elevation=random.random()) for _ in
              range(100000)]


print(f"regulart class {asizeof.asizeof(new_points)}")
print()
print(f" dataclass {asizeof.asizeof(points)}")
print()
print(f"Pydantic {asizeof.asizeof(pydantic_points)}")

print()


print(f"profit {asizeof.asizeof(points) / asizeof.asizeof(new_points)}")
print(f"profit {asizeof.asizeof(pydantic_points) / asizeof.asizeof(new_points)}")

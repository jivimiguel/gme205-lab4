from dataclasses import dataclass
from shapely.geometry.base import BaseGeometry

class SpatialObject:
    def __init__(self, geometry: BaseGeometry):
        self.geometry = geometry

    def area(self) -> float:
        return float(self.geometry.area)

@dataclass
class Parcel(SpatialObject):
    parcel_id: int
    zone: str
    is_active: bool = True
    area_sqm: float = 0.0
    geometry: BaseGeometry | None = None

    def __post_init__(self):
        if self.geometry is None:
            raise ValueError("Parcel.geometry is required")
        super().__init__(self.geometry)
from shapely.geometry import shape

class SpatialObject:
    def __init__(self, geometry):
        pass

class Parcel(SpatialObject):
    def __init__(self, parcel_id, zone, is_active, area_sqm, geometry):
        super().__init__(geometry)
        self.parcel_id = parcel_id
        self.zone = zone
        self.is_active = is_active
        self.area_sqm = area_sqm
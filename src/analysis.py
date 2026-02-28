from typing import List, Dict, Iterable, Union
from collections.abc import Iterable as IterableABC

ZonesLike = Union[str, IterableABC[str]]

def _normalize_zones(zone: ZonesLike) -> list[str]:
    if isinstance(zone, str):
        return [zone]
    return [z for z in zone if z]

def total_active_area(parcels: List) -> float:
    total = 0.0
    for p in parcels:
        if getattr(p, "is_active", False):
            total += float(p.area())
    return float(total)

def parcels_above_threshold(parcels: List, threshold: float) -> List:
    result: List = []
    th = float(threshold)
    for p in parcels:
        if float(p.area()) > th:
            result.append(p)
    return result

def count_by_zone(parcels: List) -> Dict[str, int]:
    counts: Dict[str, int] = {}
    for p in parcels:
        z = getattr(p, "zone", None)
        if not z:
            continue
        counts[z] = counts.get(z, 0) + 1
    return counts

def intersecting_parcels(parcels: List, zone: ZonesLike) -> List:
    zones = set(_normalize_zones(zone))
    result: List = []
    for p in parcels:
        if getattr(p, "zone", None) in zones:
            result.append(p)
    return result
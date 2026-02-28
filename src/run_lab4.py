import json
from pathlib import Path
from typing import List, Dict, Union
from collections.abc import Iterable

from src.spatial import Parcel
from src import analysis

DEFAULT_THRESHOLD = 300.0
DEFAULT_ZONE = "Residential"

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "parcels_shapely_ready.json"
OUTPUT_PATH = ROOT / "output" / "summary.json"

def _to_geometry(g):
    try:
        from shapely.geometry import shape
        from shapely import wkt
    except Exception:
        return g
    if isinstance(g, dict):
        return shape(g)
    if isinstance(g, str):
        try:
            return wkt.loads(g)
        except Exception:
            pass
    return g

def load_parcels(json_path: Path) -> List[Parcel]:
    with open(json_path, "r", encoding="utf-8") as f:
        raw = json.load(f)
    parcels: List[Parcel] = []
    for rec in raw:
        parcels.append(
            Parcel(
                parcel_id=rec["parcel_id"],
                zone=rec.get("zone"),
                is_active=bool(rec.get("is_active", True)),
                area_sqm=float(rec.get("area_sqm", 0.0)),
                geometry=_to_geometry(rec.get("geometry")),
            )
        )
    return parcels

ZonesLike = Union[str, Iterable[str]]

def build_summary(parcels: List[Parcel], threshold: float, desired_zone: ZonesLike) -> Dict:
    total = analysis.total_active_area(parcels)
    big = analysis.parcels_above_threshold(parcels, threshold)
    counts = analysis.count_by_zone(parcels)
    if not isinstance(counts, dict):
        counts = dict(counts)
    suitable = analysis.intersecting_parcels(parcels, desired_zone)
    zones = [desired_zone] if isinstance(desired_zone, str) else list(desired_zone)

    summary = {
        "inputs": {
            "threshold": threshold,
            "desired_zone": zones,
            "parcel_count": len(parcels),
        },
        "results": {
            "total_active_area": total,
            "large_parcels_count": len(big),
            "large_parcels_ids": [p.parcel_id for p in big],
            "zone_counts": counts,
            "suitable_parcel_ids": [p.parcel_id for p in suitable],
        },
    }
    return summary

def main(threshold: float = DEFAULT_THRESHOLD, desired_zone: ZonesLike = DEFAULT_ZONE):
    parcels = load_parcels(DATA_PATH)

    if not parcels:
        print("No parcels found.")
        return

    summary = build_summary(parcels, threshold, desired_zone)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=4)

    print("Analysis complete.")
    print(f"- Parcels loaded: {summary['inputs']['parcel_count']}")
    print(f"- Total active area: {summary['results']['total_active_area']:.4f}")
    print(f"- Large parcels (> {threshold}): {summary['results']['large_parcels_count']}")
    print(f"- Zone counts: {summary['results']['zone_counts']}")
    dz = ', '.join(summary['inputs']['desired_zone'])
    print(f"- Suitable ({dz}): {len(summary['results']['suitable_parcel_ids'])}")
    print(f"Saved: {OUTPUT_PATH}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        import traceback
        traceback.print_exc()
        print("ERROR TYPE:", type(e).__name__)
        print("ERROR MSG:", e)
# Structured Programming + Object Systems Integration
## Overview

---

## Environment Setup
- Python 3.14
- `shapely`

---

## How to Run
1. Activate the virtual environment

---

## Design
### Algorithm
I. Start
II. Load `parcels.json`
III. Convert each record into Parcel objects
IV. If no parcels exist
        - Display error message
        - Stop program
V. Initialize analysis
VI. Compute:
        - Total area of all active parcels
        - Parcels exceeded the 300 sqm area
        - Number of parcels for each `zone`
        - Parcels intersected a proposed development boundary
VII. End

### Pseudocode
BEGIN
    LOAD `parcel_data` from JSON file

    CONVERT `parcel_data` into Parcel objects
    STORE in `parcel_list`

    IF `parcel_list` is empty THEN
    PRINT "No parcels found."
    STOP
    END IF

    SET `total_active_area` = total_active_area(parcel_list)`
    SET `large_parcels` = parcels_above_threshold(parcel_list, threshold)
    SET `zone_counts` = count_by_zone(parcel_list)
    SET `intersecting` = intersecting_parcels(parcel_list, desired_zone)

    SAVE `summary.json`
END
# Structured Programming + Object Systems Integration
## Overview
This laboratory integrates structured programming with object‑oriented spatial modeling. The goal is to design a system that loads parcel data, represents each parcel as an object with spatial behavior, performs structured analysis, and produces a clean summary output. The exercise reinforces the importance of sequence, selection, repetition, and clear responsibility boundaries between objects, analysis logic, and program flow.

---

## Environment Setup
- Python 3.14
- `shapely`

---

## How to Run
1. Activate the virtual environment
2. Run `src.run_lab4`
3. The script loads data, performs analysis, prints results, and saves `output/summar.json`.

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

VII. Assemble summary `dict` and save as `summary.json`

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

    SET threshold = 300.0
    SET desired_zone = "Residential"

    SET `total_active_area` = total_active_area(parcel_list)`
    SET `large_parcels` = parcels_above_threshold(parcel_list, threshold)
    SET `zone_counts` = count_by_zone(parcel_list)
    SET `intersecting` = intersecting_parcels(parcel_list, desired_zone)

    SAVE `summary.json`
END

## Reflection
In this laboratory, I saw how much clearer the whole system becomes when I intentionally apply structured programming. The sequence in my runner—loading data, creating objects, running the analysis, and finally saving the results makes the whole workflow predictable and easy to follow. Selection appears in meaningful points like checking whether any parcels were loaded and filtering them based on activity, thresholds, or zones, while repetition naturally lives inside the analysis functions that loop through the dataset. Planning the algorithm ahead of time kept the structure clean without that step, I would have probably mixed responsibilities and ended up with a harder to maintain script.

I also learned how important it is to keep spatial behavior inside the object itself, so the analysis layer only focuses on interpreting rules rather than handling geometry. This is why `analysis.py` is the home for the rule logic instead of the demo or runner. I realized that pushing all filtering inside the Parcel class would overload it and move the system toward a God class, making it rigid and difficult to extend. Thinking about possible new rules, like excluding inactive industrial parcels also made me appreciate how easy it is to adapt the system when behavior, logic, and flow are clearly separated. Overall, this structure made the whole design more organized, scalable, and conceptually easier to understand.
# Data-driven-surrogate-model-for-predicting-thermal-performance-in-engine-cooling-jackets

## Project Overview

For my project, I am developing a **data-driven surrogate model** to predict flow and thermal performance in engine cooling jackets. The main goal is to **reduce computation time** compared to full CFD simulations:

- CFD simulation time: ~8 hours per case
- ML prediction time: < 1 minute

This allows me to quickly explore different flow and temperature conditions without running full CFD each time.

## Objective

- Run CFD simulations for a cooling channel wedge in OpenFOAM.
- Extract velocity(`U`) and pressure(`p_rgh`) data.
- Generate visualizations to understand the flow qualitatively.
- Prepare CSV data for ML model training.

## Work Done: First Run Case (U = 1.2 m/s, T = 350 K)
- **Solver:** `simpleFoam` (Laminar, Stokes stress)
- **Mesh:** Wedge mesh (bounding box: 0 <= x <= 0.1 m, 0 <= y <= 0.02 m, 0 <= z <= 0.001 m)
- **Time steps:** 100 --> 1000
- **Post-processing I did:**
  - Extracted **average celocity and pressure** per time-step using `extract_fields.py`.
  - Generated **surface and 3D glyph visualizations** in Paraview.
  - Saced CSV file: `fields_avg_timeseries.csv`.
- **Files included:**
  - `fields_avg_timeseries.csv`
  - PNGs in `visualizations/`
  - Optional VTK files in `VTK/`
## Next Steps

- I plan to run additional cases varying **velocity and temperature**, aiming for **10-50 runs** .
- This workflow will generate a dataset for training ML models, enabling fast multiple operating conditions.

## How to use
1. Open `fields_avg_timeseries.csv` to see average to see average velocity and pressure values.
2. Use the PNGs in `visualizations/` for qualitative flow understanding.
3. Run `extract_fields.py` if you want to regenerate CSVs from OpenFOAM results.

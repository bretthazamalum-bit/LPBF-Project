# LPBF Project

SJSU MSME project for automating Laser Powder Bed Fusion (LPBF) orientation
studies with SolidWorks and Ansys Mechanical.

## Licensing investigation

The project was tested with Ansys Mechanical 2026 R1 (v261) and an Ansys
academic license. The important observations are:

- A full LPBF simulation runs successfully when opened through Workbench.
- A standalone PyMechanical session can launch the visible Mechanical GUI and
  connect through gRPC.
- Opening the original `ANSYS/lpbfsim.mechdb` from the Python-launched session
  produces these Mechanical messages:

  ```text
  The database will be opened in read-only mode.
  Your license configuration does not allow Additive Manufacturing capabilities.
  Result file missing: Project > Model > Transient Thermal > Solution
  ```

- The feature tree contains question marks in the Python-launched session,
  although it previously showed green checks in Ansys 2025.
- PyMechanical's license inspection reported these enabled base products:

  ```text
  Ansys Mechanical Enterprise
  Ansys Mechanical Enterprise PrepPost
  Ansys Motion PrepPost
  Ansys Emag
  ```

The current Python runner explicitly uses `start_license="ansys"`. In
PyMechanical, that keyword requests the Ansys Mechanical Enterprise license;
it does not demonstrate that the Additive Suite capability was acquired.
Workbench appears to acquire the academic/AM entitlement through its own
license-selection and license-sharing path.

Ansys documentation states that LPBF/PBF simulation requires an Additive Suite
license. Therefore, the leading explanation is a difference between the
Workbench license context and the standalone Python license context, rather
than an inability of the `.mechdb` file to run at all.

## Database and sidecar findings

Only `ANSYS/lpbfsim.mechdb` is kept as the repository template. Solver state,
result files, lock files, license-check copies, and PyMechanical logs are
generated at runtime and excluded from version control. The runner creates
disposable copies under `ANSYS/run_work/` and removes stale run sidecars before
opening them.

A disposable copy of the `.mechdb` without the original solver sidecar opened
through PyMechanical, so the template does not require checked-in solver
outputs to run.

## ANSYS runner layout

The ANSYS workflow is split into three layers:

- `ANSYS/run_lpbf_simulation.py` is the command-line entry point and phase
  orchestrator.
- `ANSYS/lpbf/` contains host-side session, configuration, and embedded-script
  loading helpers.
- `ANSYS/mechanical_scripts/` contains the scripts executed inside Mechanical:
  geometry deletion/import, meshing, solving, and result/screenshot export.

The original `ANSYS/lpbfsim.mechdb` remains the template. Each run opens a
disposable copy under `ANSYS/run_work/`; the template is not modified.

## SolidWorks runner layout

`solidworks_workflow.py` is the thin command-line orchestrator. Its reusable
SolidWorks API code is organized under `solidworks_tools/`:

- `config.py` contains defaults and SolidWorks file-load error descriptions.
- `com_session.py` owns the single COM session and cleanup behavior.
- `documents.py` opens and activates the selected part.
- `bodies.py` reads bodies, center of mass, and bounding boxes.
- `transforms.py` rotates around the part center of mass and translates bodies.
- `placement.py` keeps rotated parts inside the plate and applies the LPBF gap.
- `interference.py` provides exact-interference and bounding-box diagnostics.
- `export.py` writes and verifies the STEP output.

These are modules in one process rather than separate scripts. That keeps all
SolidWorks COM references in the same session and preserves the template by
closing unsaved Move/Copy Body features after each export.

### Selecting the SolidWorks part

When `main.py` is started without `--part-file`, it opens a file-selection
popup for the SolidWorks `.SLDPRT` file to analyze. The selected file is passed
through the existing workflow, while the internal SolidWorks body names remain
`part` and `base`.

After selecting the part, the program asks for separate mesh sizes for the
part and build base. The part size controls the part/cartesian mesh, while the
base size controls the base sizing. The values are stored in the run manifest
and passed to every Ansys orientation solve.

For scripted or batch runs, the popup can be bypassed explicitly:

```powershell
python main.py --part-file "C:\Parts\bracket.SLDPRT" `
  --part-mesh-size-mm 0.8 --base-mesh-size-mm 1.5
```

If the mesh-size options are omitted, the program prompts for them using
defaults of `0.1 mm` for the part and `0.5 mm` for the base.

## Recommended next step

Compare the licenses shown in Ansys Licensing Settings while a Workbench LPBF
solve is active with the licenses available to the Python session. If Python
does not acquire the Additive Suite capability, start Mechanical from
Workbench and attach Python to that already-licensed session, or test a runner
that omits `start_license="ansys"` and uses Ansys's default license preference
order.

Ansys 2026 R1 was tested for backward compatibility with databases from 2025
R1 and 2025 R2. A 2025-to-2026 migration may still affect individual objects,
but the explicit Additive Manufacturing license error is the immediate cause
of the read-only state observed here.

### Orientation results

Each Ansys run writes its detailed result to a per-orientation JSON file in
`results/` and appends a flat record to `results/orientation_results.csv`.
The CSV is intended for optimization loops: it includes the X/Y/Z rotation,
numeric average, maximum, and minimum equivalent stress in Pa, run status,
timestamps, and references to the STEP and JSON files. Failed runs are also
recorded with `status=failed` and an error message so an optimizer can reject
invalid orientations instead of treating them as missing data.

After each completed orientation, the controller prints a progress line with
the current iteration, average stress, and best-so-far stress. It also refreshes
the dependency-free graph `results/stress_progress.svg`, which plots average
stress against evaluation number and shows the best-so-far trend.

Run the Bayesian controller with:

```powershell
python main.py --optimize --optimization-iterations 40
```

The default search range is 0–180 degrees on each axis with 15-degree
candidate spacing. Use `--optimization-min-angle`,
`--optimization-max-angle`, and `--optimization-grid-step` to change it.

The Ansys solve stage uses the `My Computer` local configuration, leaves
distributed solving disabled, and requests a maximum of 16 solver cores for
each run. Actual utilization can still be lower if the selected analysis or
license does not support all requested cores.

Each run also creates an `LPBF Fixed Support` in the `Static Structural`
analysis. The runner identifies the horizontal face on the global `z=0`
plane by its centroid and face normal, prioritizing the imported build-base
body. This support is added only to the disposable run copy; the repository
template remains unchanged.

After a successful solve, the runner also exports the selected equivalent-
stress viewport as a 1920x1080 PNG beside the JSON result, using names such as
`results/bo_017_equivalent_stress.png`. Screenshot export errors are recorded
in the JSON diagnostics without invalidating an otherwise successful solve.

The SolidWorks exporter rotates the part around its center of mass, then uses
the rotated world-coordinate bounding boxes to move the part in one operation.
The part's lowest Z point is placed at least 2.0 mm above the base's highest Z
point, leaving a build gap for additive support generation even after an
upside-down rotation. The minimum gap is controlled by `--support-lift-mm` when
calling `solidworks_workflow.py`; set it to `0` to disable the extra gap.

The default workflow is the Sobol plus multi-start contour workflow. It can be
started with:

```powershell
python main.py --optimization-iterations 40
```

Contour mode first evaluates explicit X/Y flip anchors, then an 8-point,
dependency-free 2-D Sobol design, and finally searches 15-degree local contour
neighborhoods around the three lowest-stress measured orientations. This
multi-start refinement keeps separate promising basins alive instead of
following only the first incumbent. If the best result does not improve for
the configured patience window, the local contour spacing is halved and the
search continues. Refinement stops after the minimum contour spacing is
reached and the best average stress has improved by less than 5% for the
patience window, or when the maximum evaluation cap is reached. The search
range and stopping behavior can be changed with
`--contour-step`, `--contour-min-step`, `--stop-improvement`,
`--stop-patience`, `--contour-starts`, and `--optimization-iterations`.

Contour candidate selection is exploitation-first: the candidate with the
lowest predicted average stress is preferred, with expected improvement used
as a tie-breaker. This keeps the search focused near the best measured
orientation. The progress graph still shows both the measured stress values
and the monotonic best-so-far curve; exploratory points may remain above that
curve.

Contour mode begins with an 8-point, dependency-free 2-D Sobol design by
default, then switches to multi-start local contour refinement. Rotation about
Z is fixed at 0 degrees because raster direction is configured independently in
ANSYS. Change the
initial design size with `--sobol-initial-runs`, the number of contour basins
with `--contour-starts`, or set the Sobol count to zero to start directly with
contour refinement. The same user-selected part and base mesh sizes are used
for every evaluation. `--contour-map` remains as an explicit compatibility
alias for the default contour workflow.

The Bayesian controller remains available as an alternative with:

```powershell
python main.py --optimize --optimization-iterations 40
```

Contour mode adds explicit baseline and X/Y flip anchors. ANSYS still runs the
complete model for every selected orientation; no symmetry reduction is applied
inside the solver. The legacy symmetry command-line options are retained for
compatibility but are ignored because Z rotation is fixed at 0 degrees.

The controller rejects missing or non-positive stress values as invalid. Invalid
orientations remain recorded in the CSV but are excluded from optimization and
are not selected again. Each JSON result also includes the selected analysis,
solution status, and result-tree diagnostics to make failed or incomplete Ansys
solves easier to investigate.

### Validated end-to-end run

The current contour workflow was validated through SolidWorks export and Ansys
Mechanical solve. The best measured point in that run was:

```text
Orientation: X=15°, Y=15°, Z=15°
Average equivalent stress: 78.12 MPa
Maximum equivalent stress: 701.21 MPa
Baseline average stress: 88.24 MPa
Improvement: 11.5%
```

The original `ANSYS/lpbfsim.mechdb` remains a template. Every run opens a
disposable copy under `ANSYS/run_work/`, so solver state is not saved back into
the template.

The fixed-support setup was verified with a baseline solve: both the transient
thermal and static structural analyses completed with status `Done`, and the
static structural result extraction returned nonzero average and maximum stress
values.

### Post-processing results

Use the dependency-free analyzer after a run to identify the optimized
orientation and create a contour-style SVG map from the measured orientations:

```powershell
python analyze_orientation_results.py
```

It reads `results/orientation_results.csv` and the per-orientation JSON files,
then writes:

- `results/orientation_summary.txt` — successful/failed counts, the lowest
  average-stress orientation, the lowest maximum-stress orientation, stress
  improvement from the zero-degree baseline, file paths, and the top ten results.
- `results/orientation_contour_map.svg` — an interpolated Rx/Ry stress map for
  the Rz slice containing the most successful results, with measured points and
  the best point marked.
- `results/orientation_contour_map.png` — PNG rendering of the contour map when
  a local SVG renderer is available.

At the end of a normal optimization run, `main.py` also writes
`results/run_summary.txt` with the run start/end time, total runtime, selected
part, mesh sizes, requested solver cores, workflow type, number of evaluations,
stress reduction from baseline, best orientations, and output-file paths. The
controller also refreshes `results/stress_progress.png` beside the live
`stress_progress.svg`. SVG labels use collision-aware placement so close
evaluations do not overwrite one another.

The default optimization target is average equivalent stress. To map and rank
by maximum stress instead, run:

```powershell
python analyze_orientation_results.py --metric max
```

### Material configurations

When launched normally, the main workflow shows a material-selection popup.
For unattended runs it also accepts `--material` with these values:

```powershell
python main.py --material inconel_718
python main.py --material 316l_stainless_steel
python main.py --material ti_6al_4v
```

The JSON files under `materials/` select ANSYS Engineering Data material
records and retain literature room-temperature ranges for sanity checking.
The ANSYS temperature-dependent material card remains authoritative. The
print-part material is assigned automatically; the configured base material
is recorded, but the base body keeps the template's current material unless
that material card has first been loaded into the Engineering Data project.

Use `--output-dir` to isolate a run's generated files from the project-level
folders:

```powershell
python main.py --part-file "C:\Parts\bracket.SLDPRT" `
  --material 316l_stainless_steel `
  --part-mesh-size-mm 0.8 --base-mesh-size-mm 2.0 `
  --output-dir "results\bracket"
```

The selected directory receives its own `generated_steps` and `results`
subdirectories, including CSV/JSON results, screenshots, graphs, maps, and
the run summary. If omitted, the original project-level folders are used.

For multiple parts or mesh cases, use the CSV batch runner:

```powershell
python batch_runner.py --csv batch_runs_sample.csv
```

Optimizer settings are kept separately in `optimizer_settings.csv`, so the
same Sobol and contour behavior can be applied to many part rows without
duplicating optimizer columns in the part manifest. The batch runner loads this
file automatically; use `--optimizer-config` to select another one.

The provided settings retain 8 Sobol evaluations, use one contour refinement
start, and stop after five consecutive evaluations improve the best stress by
less than 1%, subject to the minimum evaluation count and the per-row maximum.

ANSYS LPBF process settings are kept separately in `process_settings.csv`.
This includes solver cores, layer/deposition thickness, hatch spacing, scan
speed, dwell time, build and cooldown temperatures, base temperature, raster
angles, stripe width, beam power, beam diameter, absorptivity, and heat-source
count. The batch runner loads it automatically; use `--process-config` to select
another process file.

It runs cases sequentially and derives a unique folder from the run name,
part, material, part mesh, and base mesh. A 1 mm and 2 mm case for the same
part therefore receive separate output folders automatically.

For runs containing multiple Z-rotation slices, select one explicitly with
`--rz 0`. The SVG is generated without matplotlib or other third-party
packages and can be opened directly in a browser or imported into a report.

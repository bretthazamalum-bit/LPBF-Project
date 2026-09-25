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

## Python diagnostics

The following diagnostic scripts are in `ANSYS/`:

- `check_mechanical_license.py` launches visible Mechanical first, probes the
  remote session, and can open the template afterward.
- `check_available_licenses.py` starts Mechanical in read-only mode and prints
  the license preference list and enabled/disabled statuses without requesting
  a solve license.

The project uses the root `.venv` virtual environment. From the repository
root, examples are:

```powershell
.venv\Scripts\python.exe ANSYS\check_available_licenses.py
.venv\Scripts\python.exe ANSYS\check_mechanical_license.py --open-template --keep-open
```

For a direct test of the original template, use:

```powershell
.venv\Scripts\python.exe ANSYS\check_mechanical_license.py --open-template --use-original --keep-open
```

This direct mode does not save the original file.

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

Run the Bayesian controller with:

```powershell
python main.py --optimize --optimization-iterations 10
```

The default search range is 0–90 degrees on each axis with 15-degree
candidate spacing. Use `--optimization-min-angle`,
`--optimization-max-angle`, and `--optimization-grid-step` to change it.

The Ansys solve stage requests a maximum of 6 solver cores for each run.
Actual utilization can still be lower if the selected analysis or license
does not support all requested cores.

For adaptive local contour mapping around the best previous orientation, run:

```powershell
python main.py --contour-map --optimization-iterations 10
```

Contour mode starts with a 15-degree neighborhood, uses the accumulated CSV
results to choose the next contour point, and stops after three consecutive
successful evaluations improve the best average stress by less than 5% (after
at least five evaluations). The search range and stopping behavior can be
changed with `--contour-step`, `--stop-improvement`, and `--stop-patience`.

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

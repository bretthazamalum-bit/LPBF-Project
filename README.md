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

`ANSYS/lpbfsim.mechdb` is accompanied by `ANSYS/lpbfsim_Mech_Files/`, which
contains prior solver state and results (`.rst`, `.rth`, `.out`, `.err`, `.log`,
and related files). It also contained a top-level `.mech_lock` and solver lock
files. The top-level `.mech_lock` was removed during local testing after all
Ansys processes were closed. The remaining sidecar files were not removed.

A disposable copy of the `.mechdb` without the original sidecar opened through
PyMechanical and accepted `ExtAPI.DataModel.Project.Save()`. This shows that
the database is writable in a licensed-capable session, but it does not prove
that the original Workbench/AM license context is available to standalone
Python.

## Python diagnostics

The following diagnostic scripts are in `ANSYS/`:

- `check_mechanical_license.py` launches visible Mechanical first, probes the
  remote session, and can open the template afterward.
- `check_available_licenses.py` starts Mechanical in read-only mode and prints
  the license preference list and enabled/disabled statuses without requesting
  a solve license.

The local test runtime used Python 3.13.15. On a workstation with the local
runtime available, examples are:

```powershell
work\python313\python.exe ANSYS\check_available_licenses.py
work\python313\python.exe ANSYS\check_mechanical_license.py --open-template --keep-open
```

For a direct test of the original template, use:

```powershell
work\python313\python.exe ANSYS\check_mechanical_license.py --open-template --use-original --keep-open
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

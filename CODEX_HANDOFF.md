# LPBF Project — Codex handoff

This file is a handoff for the next ChatGPT/Codex instance. The remote desktop may wipe conversation history, so start here.

## Repository

- Upstream: https://github.com/bretthazamalum-bit/LPBF-Project
- Local working copy: `LPBF-Project-main`
- Main entry point: `main.py`
- Ansys runner: `ANSYS/run_lpbf_simulation.py`
- Mechanical template: `ANSYS/lpbfsim.mechdb`
- SolidWorks input: `Solidworks/Part1.SLDPRT`

## Environment

The project uses this virtual environment:

```text
LPBF-Project/.venv/Scripts/python.exe
```

Installed and verified packages:

- `pywin32`
- `ansys-mechanical-core==0.13.2`

Use the explicit interpreter path above rather than relying on PATH in a fresh terminal.

## What has been verified

1. SolidWorks launches and opens `Solidworks/Part1.SLDPRT`.
2. The body named `part` and base named `base` are found.
3. Rotation/collision handling completes.
4. A STEP file is exported under `generated_steps`.
5. A visible Ansys Mechanical GUI can be launched from PyMechanical.
6. The copied template opens in that visible GUI session.

## Licensing finding

The academic entitlements are Shared Web licenses, including Academic Research Mechanical (1 task) and Academic Teaching Mechanical. The Ansys licensing log shows successful checkout of the generic `ansys` feature, but attempts to use `mech_1` fail with “No such feature exists.” Other attempts reported “Maximum licensed number of demo users already reached.”

Do not replace `start_license="ansys"` with `mech_1` or `mech_2`; those features are not present in the academic license shown by the user. Workbench-first startup may be needed so Ansys uses the logged-in academic entitlement instead of the generic/demo path.

## Current code changes

`ANSYS/run_lpbf_simulation.py` currently:

- launches Mechanical visibly with `launch_mechanical(..., batch=False)`;
- uses the detected v261 executable;
- requests `start_license="ansys"`;
- opens the run copy through `ExtAPI.DataModel.Project.Open(...)`;
- removes stale generated run sidecars before opening;
- force-closes `AnsysWBU.exe` and `RunWB2.exe` before launching, to release seats.

The GUI test reached `template opened in visible Mechanical GUI`. It then stopped because the remote GUI object does not have the embedded API methods `save()` and `script_engine`. The next edit should route those operations through `mechanical_session.run_python_script(...)`:

- replace `mechanical_session.save()` with a script such as `ExtAPI.DataModel.Project.Save()`;
- update `execute_writable_script()` to call `mechanical_session.run_python_script(script)` when that method exists, retaining the embedded-engine fallback if needed.

## Recommended next steps

1. Fix the two GUI-session API calls described above.
2. Test with all Ansys GUI processes closed.
3. If the demo-user error returns, open Workbench visibly and log in first, then create/open Mechanical through Workbench. A Workbench journal may be needed to automate this.
4. Confirm the academic Mechanical seat is available before running the FEA.
5. Run `main.py` and inspect `results/` for JSON output.

## Useful commands

From the repository directory:

```powershell
$py = ".\\.venv\\Scripts\\python.exe"
& $py -m py_compile main.py solidworks_workflow.py ANSYS\\run_lpbf_simulation.py
& $py main.py
```

The generated STEP and run-copy Mechanical files are disposable. Preserve `ANSYS/lpbfsim.mechdb` and the source SolidWorks part.

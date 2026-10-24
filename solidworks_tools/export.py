"""SolidWorks STEP export."""

import os
from pathlib import Path


def export_step(model, output_file: Path):
    os.makedirs(output_file.parent, exist_ok=True)
    model.ClearSelection2(True)
    save_status = model.SaveAs3(str(output_file), 0, 0)
    if not output_file.exists():
        raise RuntimeError(
            f"STEP export did not create the expected file: {output_file}. "
            f"SaveAs3 status: {save_status}"
        )
    print(f"Exported to: {output_file}")
    print(f"SaveAs3 status: {save_status}")


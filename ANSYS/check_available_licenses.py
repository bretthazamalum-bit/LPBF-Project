"""List Mechanical license preferences and statuses for the current user.

The app starts in read-only mode, so this check does not request a solve
license. It is intended to compare the licenses visible to PyMechanical with
the license Workbench selects.
"""

from __future__ import annotations

from ansys.mechanical.core import App


def main() -> int:
    print("Starting Mechanical in read-only mode for license inspection...")
    app = App(readonly=True, version=261)

    try:
        manager = app.license_manager
        licenses = manager.get_all_licenses()

        print("\nLicense preference list:")
        for index, name in enumerate(licenses):
            print(f"  {index}: {name}")

        print("\nLicense status:")
        for name in licenses:
            print(f"  {name}: {manager.get_license_status(name)}")

        print(f"\nMechanical read-only state: {app.readonly}")
    finally:
        app.exit()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

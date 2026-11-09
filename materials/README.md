# Material configurations

These JSON files select the material records already supplied by ANSYS
Engineering Data. They do not replace ANSYS's temperature-dependent curves
with a few room-temperature constants.

The `literature_reference` section is a room-temperature sanity-check range
for reviewing the selected ANSYS material card. It is not used as a substitute
for the built-in material data. Powder condition, density, heat treatment,
porosity, build direction, and test standard can move reported values outside
these ranges.

Supported material IDs:

- `inconel_718` -> ANSYS `Inconel 718`
- `316l_stainless_steel` -> ANSYS `316L Stainless Steel`
- `ti_6al_4v` -> ANSYS `Ti - 6 Al - 4 V`

The build-process settings remain separate from material identity. In
particular, laser power, hatch spacing, layer thickness, scan speed, and
preheat must be calibrated for the printer, powder, and material rather than
copied between these three alloys automatically.

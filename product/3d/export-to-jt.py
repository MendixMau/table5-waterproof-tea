# OSME DryTea CONTROL — FreeCAD model + JT export
#
# HOW TO RUN:
#   1. Install FreeCAD: https://www.freecad.org/downloads.php
#   2. Open FreeCAD → Tools → Macro → Macros... → Create new
#   3. Paste this entire file, click Run (or use: freecadcmd dryteacontrol-freecad.py)
#
# OUTPUT: C:/Mendix/OSME_DryTea_CONTROL.jt
#
# All dimensions in millimetres, based on designer.png reference image.

import FreeCAD as App
import Part
import math
import os

OUTPUT_PATH = "C:/Mendix/OSME_DryTea_CONTROL.jt"
doc = App.newDocument("OSME_DryTea_CONTROL")

# ── Helpers ────────────────────────────────────────────────────────────────

def cylinder(r, h, z_offset=0):
    s = Part.makeCylinder(r, h)
    s.translate(App.Vector(0, 0, z_offset))
    return s

def tube(r_outer, r_inner, h, z_offset=0):
    outer = cylinder(r_outer, h, z_offset)
    inner = cylinder(r_inner, h, z_offset)
    return outer.cut(inner)

def add_part(shape, name, label, color=(0.8, 0.8, 0.8)):
    obj = doc.addObject("Part::Feature", name)
    obj.Shape = shape
    obj.Label = label
    obj.ViewObject.ShapeColor = color
    return obj

# ── 1. Control Rod + Seals ─────────────────────────────────────────────────
# Rod: Ø3mm × 58mm, centred on assembly axis
rod_body = cylinder(1.5, 58, -29)

# Top handle disc
handle_disc = cylinder(7, 2.5, 30)
handle_knob = cylinder(3.5, 5, 32.5)
handle = handle_disc.fuse(handle_knob)

# Seals (rubber O-ring discs)
seal_upper = cylinder(8, 3, 2)
seal_lower = cylinder(8, 3, -18)

rod_assembly = rod_body.fuse(handle).fuse(seal_upper).fuse(seal_lower)
add_part(rod_assembly, "ControlRod", "Control Rod + Seals", (0.78, 0.78, 0.78))

# ── 2. Sliding Waterproof Sleeve ───────────────────────────────────────────
# Sleeve: Ø28mm outer / Ø25mm inner × 42mm
sleeve_body = tube(14, 11.5, 42, -21)

# Grip ridges (4 × Ø0.8mm torus approximated as thin rings)
ridges = []
for z in [-8, -2, 4, 10]:
    ridge = tube(14.8, 14, 1.2, z - 0.6)
    ridges.append(ridge)

sleeve_shape = sleeve_body
for r in ridges:
    sleeve_shape = sleeve_shape.fuse(r)

add_part(sleeve_shape, "Sleeve", "Sliding Waterproof Sleeve", (0.24, 0.73, 0.61))

# ── 3. Porous Inner Tea Filter ─────────────────────────────────────────────
# Filter: Ø23mm outer / Ø20mm inner × 52mm mesh cage
filter_wall = tube(11.5, 10, 52, -26)

# Top & bottom caps (solid discs with centre bore for rod)
cap_top = cylinder(11.5, 2.5, 26).cut(cylinder(2, 2.5, 26))
cap_bot = cylinder(11.5, 2.5, -28.5).cut(cylinder(2, 2.5, -28.5))

# Mesh ports: 48 small circular holes in a 6×8 grid around the cylinder
# Approximated as subtracted cylinders oriented radially
mesh_holes = []
rows = 6
cols = 8
for row in range(rows):
    z_pos = -20 + row * 8
    for col in range(cols):
        angle = (col / cols) * 2 * math.pi + (row % 2) * (math.pi / cols)
        # Small bore hole through the wall, oriented radially
        hole = Part.makeCylinder(1.0, 6)
        # Rotate to point radially outward
        hole.rotate(App.Vector(0, 0, 0), App.Vector(0, 1, 0), 90)
        # Translate to wall position
        hole.translate(App.Vector(
            math.cos(angle) * 8,
            z_pos,
            math.sin(angle) * 8
        ))
        mesh_holes.append(hole)

filter_shape = filter_wall.fuse(cap_top).fuse(cap_bot)
for hole in mesh_holes:
    try:
        filter_shape = filter_shape.cut(hole)
    except Exception:
        pass  # skip degenerate cuts

add_part(filter_shape, "TeaFilter", "Porous Inner Tea Filter", (0.78, 0.59, 0.23))

# ── 4. Outer Body + Water-Flow Ports ──────────────────────────────────────
# Outer body: Ø34mm outer / Ø29mm inner × 64mm
outer_wall = tube(17, 14.5, 64, -32)

# Top + bottom collars
collar_top = cylinder(17, 3.5, 32).cut(cylinder(14, 3.5, 32))
collar_bot = cylinder(17, 3.5, -35.5).cut(cylinder(14, 3.5, -35.5))

# 8 water-flow ports (Ø3mm, two rows of 4)
port_shape_list = []
for row, z_port in enumerate([-8, 8]):
    for col in range(4):
        angle = (col / 4) * 2 * math.pi + row * (math.pi / 4)
        port = Part.makeCylinder(1.5, 8)
        port.rotate(App.Vector(0, 0, 0), App.Vector(0, 1, 0), 90)
        port.translate(App.Vector(
            math.cos(angle) * 13,
            z_port,
            math.sin(angle) * 13
        ))
        port_shape_list.append(port)

outer_shape = outer_wall.fuse(collar_top).fuse(collar_bot)
for p in port_shape_list:
    outer_shape = outer_shape.cut(p)

add_part(outer_shape, "OuterBody", "Outer Body + Water-Flow Ports", (0.93, 0.92, 0.88))

# ── Recompute + Exploded positions for JT ─────────────────────────────────
# In JT, exploded views are stored as product structure transforms.
# We place each component in its exploded offset position so the JT
# viewer can animate back to origin (assembled).

EXPLODE_OFFSETS = {
    "ControlRod": App.Vector(0,   95, 0),
    "Sleeve":     App.Vector(65, -12, 30),
    "TeaFilter":  App.Vector(-60,  5, -20),
    "OuterBody":  App.Vector(0,  -95, 0),
}

for name, offset in EXPLODE_OFFSETS.items():
    obj = doc.getObject(name)
    if obj:
        shape = obj.Shape.copy()
        shape.translate(offset)
        obj.Shape = shape

doc.recompute()

# ── Export to JT ───────────────────────────────────────────────────────────
print("Exporting to JT…")

try:
    # FreeCAD uses OpenCASCADE's JT import/export via the ImportJT workbench
    import ImportJT
    shapes_to_export = [
        doc.getObject("ControlRod"),
        doc.getObject("Sleeve"),
        doc.getObject("TeaFilter"),
        doc.getObject("OuterBody"),
    ]
    ImportJT.export(shapes_to_export, OUTPUT_PATH)
    print(f"SUCCESS: {OUTPUT_PATH}")

except ImportError:
    # Fallback: try the Part workbench JT writer directly
    try:
        import Part as _Part
        objects = [
            doc.getObject("ControlRod").Shape,
            doc.getObject("Sleeve").Shape,
            doc.getObject("TeaFilter").Shape,
            doc.getObject("OuterBody").Shape,
        ]
        compound = Part.makeCompound(objects)
        compound.exportJt(OUTPUT_PATH)
        print(f"SUCCESS via Part.exportJt: {OUTPUT_PATH}")

    except AttributeError:
        # Last resort: export STEP and note that JT conversion is needed
        step_path = OUTPUT_PATH.replace(".jt", ".step")
        import ImportGui
        ImportGui.export(
            [doc.getObject(n) for n in EXPLODE_OFFSETS],
            step_path
        )
        print(f"NOTE: JT export not available in this FreeCAD build.")
        print(f"STEP exported to: {step_path}")
        print(f"Convert to JT via: NX → File → Import → STEP → Save As → JT")
        print(f"Or online: https://www.3dvieweronline.com (STEP → JT)")

# ── Save FreeCAD document ──────────────────────────────────────────────────
fcstd_path = OUTPUT_PATH.replace(".jt", ".FCStd")
doc.saveAs(fcstd_path)
print(f"FreeCAD document saved: {fcstd_path}")

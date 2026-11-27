# OSME Teabag Infuser — FreeCAD GLB → JT export macro
#
# HOW TO RUN:
#   1. Install FreeCAD: https://www.freecad.org/downloads.php
#   2. Open FreeCAD → Tools → Macro → Macros... → Create new
#   3. Paste this entire file and click Run
#      OR: freecadcmd osme-infuser-freecad.py
#
# INPUT:  C:/Mendix/osme-teabag-infuser-open-animated.glb
# OUTPUT: C:/Mendix/osme-teabag-infuser-open-animated.jt
#
# FreeCAD reads GLB via its built-in GLTF importer (Mesh workbench),
# then exports to JT via ImportJT workbench. Falls back to STEP if
# the JT workbench is not installed in this FreeCAD build.

import FreeCAD as App
import os

GLB_PATH  = "C:/Mendix/osme-teabag-infuser-open-animated.glb"
JT_PATH   = "C:/Mendix/osme-teabag-infuser-open-animated.jt"
STEP_PATH = "C:/Mendix/osme-teabag-infuser-open-animated.step"

doc = App.newDocument("OSME_Infuser")

# ── 1. Import GLB ──────────────────────────────────────────────────────────
print("Importing GLB…")

imported = False

# Try native GLTF/GLB importer (FreeCAD ≥ 0.21)
try:
    import ImportGLTF
    ImportGLTF.insert(GLB_PATH, doc.Name)
    doc.recompute()
    imported = True
    print("Imported via ImportGLTF")
except ImportError:
    pass

# Fallback: Mesh workbench importer (older builds)
if not imported:
    try:
        import Mesh
        Mesh.insert(GLB_PATH, doc.Name)
        doc.recompute()
        imported = True
        print("Imported via Mesh workbench")
    except Exception as e:
        print(f"Mesh import failed: {e}")

if not imported:
    raise RuntimeError(
        "No GLB importer found in this FreeCAD build.\n"
        "Install FreeCAD ≥ 0.21 or enable the GLTF workbench."
    )

# ── 2. Collect all imported objects ───────────────────────────────────────
objects = [o for o in doc.Objects if hasattr(o, "Shape") or hasattr(o, "Mesh")]
print(f"Objects imported: {[o.Label for o in objects]}")

# ── 3. Export to JT ────────────────────────────────────────────────────────
print("Exporting to JT…")

exported = False

# Primary path: ImportJT workbench
try:
    import ImportJT
    ImportJT.export(objects, JT_PATH)
    print(f"SUCCESS: {JT_PATH}")
    exported = True
except ImportError:
    print("ImportJT workbench not found, trying Part.exportJt…")

# Secondary path: Part compound exportJt
if not exported:
    try:
        import Part
        shapes = []
        for o in objects:
            if hasattr(o, "Shape"):
                shapes.append(o.Shape)
            elif hasattr(o, "Mesh"):
                # Convert mesh to shape
                shape = Part.Shape()
                shape.makeShapeFromMesh(o.Mesh.Topology, 0.1)
                shapes.append(shape)
        if shapes:
            compound = Part.makeCompound(shapes)
            compound.exportJt(JT_PATH)
            print(f"SUCCESS via Part.exportJt: {JT_PATH}")
            exported = True
    except AttributeError:
        print("Part.exportJt not available in this build.")
    except Exception as e:
        print(f"Part.exportJt error: {e}")

# Tertiary path: STEP export
if not exported:
    try:
        import ImportGui
        step_objects = [o for o in doc.Objects if hasattr(o, "Shape")]
        if step_objects:
            ImportGui.export(step_objects, STEP_PATH)
            print(f"NOTE: JT export not available. STEP exported to: {STEP_PATH}")
            print("Convert STEP → JT via:")
            print("  Siemens NX:  File → Import → STEP → Save As → JT")
            print("  Online:      https://www.3dvieweronline.com")
        else:
            # Mesh-only export via OBJ as last resort
            import Mesh as _Mesh
            mesh_objects = [o for o in doc.Objects if hasattr(o, "Mesh")]
            obj_path = STEP_PATH.replace(".step", ".obj")
            _Mesh.export(mesh_objects, obj_path)
            print(f"NOTE: Exported as OBJ (mesh): {obj_path}")
            print("Convert OBJ → JT via Siemens NX or Teamcenter.")
    except Exception as e:
        print(f"Fallback export error: {e}")

# ── 4. Save FreeCAD document ───────────────────────────────────────────────
fcstd_path = JT_PATH.replace(".jt", ".FCStd")
doc.saveAs(fcstd_path)
print(f"FreeCAD document saved: {fcstd_path}")

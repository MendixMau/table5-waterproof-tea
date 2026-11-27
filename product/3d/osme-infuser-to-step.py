# OSME Infuser — OBJ meshes → STEP (headless FreeCAD)
import FreeCAD as App
import Mesh
import Part
import os
import glob

OBJ_DIR   = "C:/Mendix/osme_meshes"
STEP_PATH = "C:/Mendix/osme-teabag-infuser-open-animated.step"

doc = App.newDocument("OSME_Infuser")

obj_files = sorted(f for f in glob.glob(f"{OBJ_DIR}/*.obj") if "OSME_combined" not in f)
print(f"Importing {len(obj_files)} OBJ files…")

shapes = []
for obj_path in obj_files:
    name = os.path.splitext(os.path.basename(obj_path))[0]
    Mesh.insert(obj_path, doc.Name)
    mo = doc.Objects[-1]
    mo.Label = name
    doc.recompute()
    try:
        shape = Part.Shape()
        shape.makeShapeFromMesh(mo.Mesh.Topology, 0.01)
        shapes.append(shape)
        print(f"  OK: {name}  ({len(mo.Mesh.Facets)} facets)")
    except Exception as e:
        print(f"  Warning {name}: {e}")

print(f"Building compound from {len(shapes)} shapes…")
compound = Part.makeCompound(shapes)

print(f"Exporting STEP to {STEP_PATH}…")
compound.exportStep(STEP_PATH)
print(f"SUCCESS: {STEP_PATH}")
print(f"File size: {os.path.getsize(STEP_PATH):,} bytes")

fcstd_path = STEP_PATH.replace(".step", ".FCStd")
doc.saveAs(fcstd_path)
print(f"FreeCAD document: {fcstd_path}")

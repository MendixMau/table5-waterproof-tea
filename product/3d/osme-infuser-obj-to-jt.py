# OSME Infuser — OBJ meshes → FreeCAD → JT export
import FreeCAD as App
import Mesh
import Part
import os
import glob

OBJ_DIR  = "C:/Mendix/osme_meshes"
JT_PATH  = "C:/Mendix/osme-teabag-infuser-open-animated.jt"
STEP_PATH = "C:/Mendix/osme-teabag-infuser-open-animated.step"

doc = App.newDocument("OSME_Infuser")

obj_files = sorted(glob.glob(f"{OBJ_DIR}/*.obj"))
# skip the combined one — use individual meshes for named structure
obj_files = [f for f in obj_files if "OSME_combined" not in f]

print(f"Importing {len(obj_files)} OBJ files…")
mesh_objects = []
for obj_path in obj_files:
    name = os.path.splitext(os.path.basename(obj_path))[0]
    Mesh.insert(obj_path, doc.Name)
    # The last inserted object is what we just added
    obj = doc.Objects[-1]
    obj.Label = name
    mesh_objects.append(obj)
    print(f"  Imported: {name}")

doc.recompute()
print(f"Total objects: {len(doc.Objects)}")

# ── Convert meshes to shapes for JT export ────────────────────────────────
print("Converting meshes to Part shapes…")
shape_objects = []
for mo in mesh_objects:
    try:
        shape = Part.Shape()
        shape.makeShapeFromMesh(mo.Mesh.Topology, 0.01)
        feat = doc.addObject("Part::Feature", mo.Name + "_shape")
        feat.Shape = shape
        feat.Label = mo.Label
        shape_objects.append(feat)
    except Exception as e:
        print(f"  Warning: {mo.Label} shape conversion failed: {e}")

doc.recompute()

# ── Export to JT ──────────────────────────────────────────────────────────
exported = False

try:
    import ImportJT
    targets = shape_objects if shape_objects else mesh_objects
    ImportJT.export(targets, JT_PATH)
    print(f"SUCCESS: {JT_PATH}")
    exported = True
except ImportError:
    print("ImportJT not available, trying Part.exportJt…")
except Exception as e:
    print(f"ImportJT error: {e}")

if not exported:
    try:
        shapes = [o.Shape for o in shape_objects if hasattr(o, "Shape")]
        compound = Part.makeCompound(shapes)
        compound.exportJt(JT_PATH)
        print(f"SUCCESS via Part.exportJt: {JT_PATH}")
        exported = True
    except AttributeError:
        print("Part.exportJt not available.")
    except Exception as e:
        print(f"Part.exportJt error: {e}")

if not exported:
    # STEP fallback
    try:
        import ImportGui
        targets = shape_objects if shape_objects else []
        if targets:
            ImportGui.export(targets, STEP_PATH)
            print(f"STEP exported: {STEP_PATH}")
        else:
            # OBJ-only fallback: export combined OBJ mesh as STL
            combined_obj = f"{OBJ_DIR}/OSME_combined.obj"
            Mesh.insert(combined_obj, doc.Name)
            stl_path = JT_PATH.replace(".jt", ".stl")
            Mesh.export([doc.Objects[-1]], stl_path)
            print(f"STL exported (mesh only): {stl_path}")
    except Exception as e:
        print(f"Fallback error: {e}")

# ── Save FCStd ─────────────────────────────────────────────────────────────
fcstd_path = JT_PATH.replace(".jt", ".FCStd")
doc.saveAs(fcstd_path)
print(f"FreeCAD document saved: {fcstd_path}")

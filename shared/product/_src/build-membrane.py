import base64, sys
from pathlib import Path
R = Path(sys.argv[1])
src = Path(__file__).with_name("membrane-how.src.html").read_text()
jost = base64.b64encode((R / "brand/assets/fonts/jost-latin.woff2").read_bytes()).decode()
(R / "shared/product/membrane-how.html").write_text(src.replace("{{JOST}}", jost))
print("ok")

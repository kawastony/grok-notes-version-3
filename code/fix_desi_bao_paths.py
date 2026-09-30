"""Rewrite stage0/stage2 yamls: strip double data/ from bao.generic paths."""
from pathlib import Path
import re

ROOT = Path("/content")
files = [
    "stage0_lcdm_desi.yaml",
    "stage0_phi_desi.yaml",
    "stage2_lcdm_planck_desi.yaml",
    "stage2_phi_planck_desi.yaml",
]

for name in files:
    p = ROOT / name
    if not p.exists():
        # also try chains restored copies
        p = Path("/content/drive/MyDrive/tafa_chains") / name.replace(".yaml", ".input.yaml")
    if not p.exists():
        print("MISSING", name)
        continue
    text = p.read_text()
    text2 = text.replace(
        "data/bao_data/desi_2024_gaussian_bao_ALL_GCcomb_mean.txt",
        "bao_data/desi_2024_gaussian_bao_ALL_GCcomb_mean.txt",
    ).replace(
        "data/bao_data/desi_2024_gaussian_bao_ALL_GCcomb_cov.txt",
        "bao_data/desi_2024_gaussian_bao_ALL_GCcomb_cov.txt",
    )
    out = ROOT / name if not name.endswith(".input.yaml") else ROOT / name.replace(".input.yaml", ".yaml")
    # write fixed run yaml under /content
    out = ROOT / name if "stage" in name and name.endswith(".yaml") else ROOT / name.replace(".input.yaml", "")
    # simpler: always write to /content/<stage>.yaml
    stage = re.sub(r"\.(input|updated)\.yaml$", ".yaml", name)
    if not stage.endswith(".yaml"):
        stage = name
    out = ROOT / Path(stage).name
    out.write_text(text2)
    print("wrote", out, "changed", text != text2)

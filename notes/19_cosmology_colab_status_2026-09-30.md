# Cosmology Colab status — 2026-09-30

## Installs
All OK: camb, planck lowl TT/EE, plik lite, lensing, bao.generic.

## Frozen-φ
w0 = −0.8090169943749475  
wa = −0.6180339887498948

## Run results

| Stage | Prefix | Exit | Chain files |
|-------|--------|------|-------------|
| 0 ΛCDM DESI | stage0_lcdm_desi | **1** | yaml only |
| 0 φ DESI | stage0_phi_desi | **1** | yaml only |
| 1 ΛCDM Planck | stage1_lcdm_planck | **0** | .1.txt, covmat, checkpoint |
| 1 φ Planck | stage1_phi_planck | **0** | .1.txt, covmat, checkpoint |
| 2 ΛCDM Planck+DESI | stage2_lcdm_planck_desi | **1** | yaml only |
| 2 φ Planck+DESI | stage2_phi_planck_desi | **1** | yaml only |

Saved under `/content/drive/MyDrive/tafa_chains` (20 files).

## Diagnosis
DESI stages fail at model build (no .txt chains). Historical causes in this project:
1. `A_planck` in params when likelihood is DESI-only (stage0)
2. bao.generic path / measurements block mismatch
3. CAMB packages_path not visible to cobaya-run subprocess

Stage1 Planck is usable **now** for ΛCDM vs frozen-φ comparison.

## Next
1. Load stage1 chains with getdist; compare H0, omegam, sigma8, ns.
2. Print stage0 yaml + cobaya error log; strip A_planck from stage0; fix bao measurements path.
3. Re-run stage0 then stage2 only after stage0 green.

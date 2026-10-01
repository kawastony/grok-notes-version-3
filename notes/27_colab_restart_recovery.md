# Colab restart recovery (2026-10-02)

User restarted runtime. Ephemeral /content is gone. Drive is source of truth.

## Already finished (do not rerun if .1.txt on Drive)
- stage1_lcdm_planck, stage1_phi_planck
- stage0_lcdm_desi, stage0_phi_desi (BAO path fix confirmed; H0 unconstrained)

## Stage 2
Was running when session died. Rerun only prefixes missing `.1.txt` on Drive.

## BAO path
measurements_file: bao_data/desi_2024_gaussian_bao_ALL_GCcomb_mean.txt
(not data/bao_data/...)

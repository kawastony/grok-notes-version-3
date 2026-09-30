# Stage 1 Planck results + DESI path fix

## Stage 1 (Planck only) — converged

| Parameter | ΛCDM | frozen-φ |
|-----------|------|----------|
| H₀ | 68.16 ± 0.73 | 67.36 ± 0.67 |
| Ωₘ | 0.3045 ± 0.0095 | 0.3115 ± 0.0092 |
| σ₈ | 0.826 ± 0.011 | 0.818 ± 0.011 |
| nₛ | 0.9693⁺⁰·⁰⁰⁴⁶₋₀.₀₀₅₁ | 0.9699 ± 0.0047 |
| Ω_b h² | 0.02252 ± 0.00017 | 0.02252 ± 0.00016 |
| Ω_c h² | 0.1182 ± 0.0016 | 0.1181 ± 0.0015 |
| τ | 0.0490⁺⁰·⁰⁰⁹⁰₋₀.₀₀₈₀ | 0.0491 ± 0.0083 |
| ln(10¹⁰ Aₛ) | 3.093 ± 0.034 | 3.083⁺⁰·⁰³⁵₋₀.₀₃₁ |

Frozen-φ: w₀ ≈ −0.809, w_a ≈ −0.618.

Shift pattern (Planck only):
- H₀ lower by ~0.8 km/s/Mpc
- Ωₘ higher by ~0.007
- σ₈ slightly lower
- nₛ, Ω_b h², Ω_c h² essentially unchanged

Contours overlap strongly; difference is within ~1σ on Planck alone. DESI BAO is the sharper late-time test.

## DESI failure root cause

```
measurements_file: data/bao_data/desi_2024_gaussian_bao_ALL_GCcomb_mean.txt
```
joined with `packages_path/data` →
`/content/packages/data/data/bao_data/...` (double `data/`)

Files actually live at:
`/content/packages/data/bao_data/desi_2024_gaussian_bao_ALL_GCcomb_mean.txt`

### Fix
```yaml
likelihood:
  bao.generic:
    measurements_file: bao_data/desi_2024_gaussian_bao_ALL_GCcomb_mean.txt
    cov_file: bao_data/desi_2024_gaussian_bao_ALL_GCcomb_cov.txt
```

Apply to stage0_lcdm_desi, stage0_phi_desi, stage2_*_planck_desi.

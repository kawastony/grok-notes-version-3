# Stream 1 on residual-gated L=10 operator densities

**Date:** 2026-10-01  
**Code:** `grok-notes-version-2/Colab_L12_residual_gated_notebook.py` (8-component Wilson–Dirac hedgehog)  
**Artifact:** `data/stream1_L10_operator_forman.json`

## Run
L=10, d=3, k=4, \(\sigma=0\) shift-invert. Mode 0 only. Gate \(r_{\rm rel}\le10^{-6}\).

| label | \((v_1,v_2)\) | \(\lambda_0\) | \(r_{\rm rel}\) | gated |
|-------|----------------|---------------|-----------------|-------|
| B | (2.0, 2.0) | +0.00139 | \(6.2\times10^{-14}\) | yes |
| T | (1.85, 2.0) | +0.00106 | \(5.5\times10^{-14}\) | yes |
| P | (1.7, 2.0) | +0.00093 | \(5.5\times10^{-14}\) | yes |

Tube from density: 126 nodes, 297 edges, 85 mid edges. Weighted Forman = v2 Stage-2 formula.

## Forman + early flow

| kind | \(F_{\mathrm{mid}}\) | \(\bar F\) | \(F^{\rm rel}\) | dW8 |
|------|----------------------|------------|-----------------|-----|
| B | **−9.284** | −8.311 | **−0.973** | **+0.0176** |
| T | −9.188 | −8.485 | −0.704 | +0.0121 |
| P | **−8.717** | −8.233 | **−0.484** | **−0.0049** |

v2 published baseline: \(F_{\mathrm{mid}}=-9.28\), \(\bar F=-8.44\), \(F^{\rm rel}=-0.84\), \(\Delta W_8=+0.088\).  
v2 polarized: \(F_{\mathrm{mid}}=-8.72\), \(F^{\rm rel}=-0.33\), \(\Delta W_8\approx0\).

This run hits the **absolute \(F_{\mathrm{mid}}\) targets**. Relative depths are the same order and the same ranking. dW8 is smaller than the published +0.088 (tube mask / mid definition) but the **sign split is the v2 one**: B feeds, P does not.

## Protocol

| Test | Call |
|------|------|
| Residual gate | **PASS** (all three) |
| S1.1 \(F^{\rm rel}\) B < T < P | **PASS** |
| S1.2 dW8 B > T > P | **PASS** |
| S1.5 Ollivier | not rerun; v2 + note 31 already flat on this geometry |

## Unlock language
This is the missing “real Stream 1” object: **residual-clean operator \(\rho\)**, not Colab chord replicas. Micro mediator \(F^{\rm rel}\to\) early feed holds on the gated L=10 pair.

Still not GR. Still not SPARC lattice-on. n=3 points — expand the 3×3 grid when you want p-values.

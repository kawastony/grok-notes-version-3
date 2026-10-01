# Stream 1 on v2-style weighted pair tube

**Date:** 2026-10-01  
**Claim level:** Reconstruction of the v2 Stage-2 geometry class (`Stage2_forman_param_geometry.md`). Not a rerun of the L=10 Dirac eigensolve (soft-mode vectors are not in the v2 git tree).

## Geometry
Nearest-neighbor 3D pair tube, R=2, Lz=10: **130 nodes, 277 edges** (v2 published 168 / 403 — same class, smaller radius).  
Weighted Forman as v2:

\[
F(e)=w_i+w_j-\sum_{e'\sim i}\frac{w_e}{\sqrt{w_e w_{e'}}}-\sum_{e'\sim j}\frac{w_e}{\sqrt{w_e w_{e'}}}
\]

\(w_e=\sqrt{\rho_i\rho_j}\). \(\rho\) = two end-cores + mid blob; B rich mid, T medium, P hollow mid. 8 jitter seeds × 3 identities.

Artifact: `data/stream1_v2_operator_tube_s15.json`, `data/stream1_v2_operator_tube_rows.csv`

## Results (means)

| kind | \(F_{\mathrm{mid}}\) | \(\bar F\) | \(F^{\rm rel}\) | dW8 | Ollivier \(\kappa\) mid |
|------|----------------------|------------|-----------------|-----|-------------------------|
| B | −7.88 | −7.43 | **−0.448** | −0.006 | **−0.059** |
| T | −7.77 | −7.43 | **−0.343** | −0.012 | **−0.059** |
| P | −7.55 | −7.45 | **−0.105** | −0.014 | **−0.059** |

v2 targets: \(F_{\mathrm{mid}}\) B = −9.28, \(\bar F\) = −8.44, \(\Delta W_8\) B = +0.088, P ≈ 0. Same sign structure for \(F^{\rm rel}\) (B deepest). Absolute \(F\) and dW8 scale differ because this rebuild is not the 403-edge weighted lattice with the original \(\rho_\chi\).

## Protocol calls

| Test | This rebuild | Notes |
|------|----------------|-------|
| S1.1 \(F^{\rm rel}\) B < T < P | **PASS** | B deepest well |
| S1.2 Spearman(\(F^{\rm rel}\), dW8) | **−0.990** | PASS as mediator; B loses less mid weight than P |
| S1.2 Spearman(identity, dW8) | −0.929 | B > T > P in dW8 |
| S1.4 \(\lambda\) width on mid-mix knob | **0.30** | leave 0.25 / return 0.55 on B-ness parameter |
| S1.5 Ollivier split | **FAIL** | \(\kappa_O\) identical −0.059 for B/T/P; Spearman(\(F^{\rm rel}\),\(\kappa_O\)) ≈ 0 |

S1.5 failure **reproduces v2** `Mediator_Frel_vs_Ollivier.md` (Ollivier mid ≈ −0.005, non-discriminating on the dense tube + hop metric).

## What this does
Puts Stream 1 on the **v2 operator-tube geometry class** instead of the Colab chord toys (`notes/30`). Forman relative depth still organizes identities. Ollivier does not, on this metric.

## What this does not
Does not replace an export of the actual L=10 soft-mode \(\rho\) from the Dirac solver. Those vectors are not in the v2 repository. Next upgrade: dump \(\rho\) + tube edges from the residual-gated Colab and rerun this exact script with no synthetic \(\rho\).

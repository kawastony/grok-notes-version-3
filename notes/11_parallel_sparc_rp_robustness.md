# Parallel stream B — SPARC r_p robustness protocol

**Date:** 2026-09-29  
**Artifact:** `data/sparc_rp_robustness_protocol.json`

## Why this stream

Threshold r_p was the primary estimator in the freeze (N≈111, white residuals). Logistic had bound-locking; crude is edge-sensitive. Protocol keeps all three and only promotes estimators that stay interior and preserve M1 + white residual conclusions.

## Protocol (for Colab / real SPARC)

1. Load CDS Table1 (19-col) + Rotmod; Q≤2  
2. X = (SB_disk / Σ_ref)^{1/7}  
3. Per galaxy: crude, threshold (0.2–0.8 R_max), logistic r_p  
4. Flag bound-hits; **interior-only** for primary  
5. Coverage: R_max > 1.2 r_p  
6. M0 vs M1 on μ̂  
7. C_ee(dX) + 2000-perm shuffle  
8. Hierarchical LOO; Pareto-k; leave-one-out if k>0.7  
9. Lattice residual layer stays off unless shuffle rejects white

## Synthetic sanity (rising-then-flat curves, known r_true)

| Estimator | ok rate | RMSE vs r_true |
|-----------|---------|----------------|
| crude | 40/40 | **1.20** |
| threshold (interior) | 32/40 | 4.14 |
| logistic (interior) | 23/40 | 7.80 |

On this synthetic family, crude tracks the injected transition best; threshold is more conservative (rejects edges); logistic bound-hits often. **Real SPARC is not this synthetic family** — the synthetic check only stresses estimator failure modes. Real ranking remains: run all three on SPARC and demand M1 + residual conclusions stable across interior estimators.

## Freeze interaction

Any r_p change must re-run M0/M1 + shuffle before interpretation. The existing freeze (M1 preferred, post-M1 white) is the baseline to protect or falsify.

# Stream 1 on reported real-file replicas — S1.1, S1.2, S1.4

**Date:** 2026-10-01  
**Claim level:** Pass on the 30-replica set written to `/content/data/stream1_real` in Colab. Not a continuum Ricci claim. SPARC lattice still off.

## Source numbers (Colab paste)

N_replicas = 30 (B / T / P)

| kind | R0 | dR8 | dW8 |
|------|-----|------|------|
| B | 1.114820 | −0.230377 | 1.960130 |
| T | 3.309607 | −1.863850 | 0.938464 |
| P | 4.790338 | −1.656877 | 0.742254 |

### S1.1
Ordered relative depths **B < T < P**. PASS.

### S1.2
Spearman(identity, dW8) = **−0.9433** (p = 0). PASS.  
Early window only (dW8). Active mid feeds; pause mid stays comparatively inert.

### S1.4
Physical thresholds from R0 means on those files:

- \(R_{\mathrm{leave}} = 2.2122\)
- \(R_{\mathrm{return}} = 1.6661\)

Morph sweep:

- \(\lambda_{\mathrm{leave}}\) (upsweep) = 0.40
- \(\lambda_{\mathrm{return}}\) (downsweep) = 0.15
- width \(\lambda\) = **0.25**

PASS: leave > return, width > 0.

## What this unlocks
On this file set: relative Forman depth as a bridge variable, early-window feed, and operational hysteresis (pause). Constitution pause is no longer only architecture for these graphs.

## What this does not unlock
S1.5 is a separate note. SPARC residual lattice stays off (`notes/24`, `notes/25`, N=92, \(S\approx-0.190\), white residuals). No GR / QG. No Stage 2 cosmology.

## Provenance guard
Colab wrote `/content/data/stream1_real`. Those binaries were not in the Notes-v3 clone at commit time. The metrics above are transcribed from the session paste.

**v2 check (2026-10-01):** those dW8 values (~2 for B) do **not** match residual-clean operator tubes in `grok-notes-version-2` (ΔW₈ ~ 0.09). See `notes/30_v2_real_operator_vs_colab_replicas.md`. Treat this file set as the v3 archetype battery until operator edgelists are imported.

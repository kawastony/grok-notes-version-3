# L=10 3×3 residual-gated grid — Stream 1

**Date:** 2026-10-01  
**Artifact:** `data/stream1_L10_3x3.json`  
**Operator:** same as note 32. Grid \(v_1,v_2\in\{1.7,2.0,2.3\}\), d=3, mode 0.  
**Class labels:** copied from v2 `Identity_propagation_3x3_results.md` (R_mid / P / H rule), not refit here.

## Gate
9/9 accepted. max \(r_{\rm rel}=9.2\times10^{-14}\).

## Means by v2 class

| class | n | \(F^{\rm rel}\) | dW8 | \(F_{\mathrm{mid}}\) |
|-------|---|-----------------|-----|----------------------|
| B | 3 | −0.730 | **+0.0173** | −8.74 |
| T | 4 | −0.824 | +0.0134 | −8.94 |
| P | 2 | −0.608 | **+0.0052** | −8.76 |

dW8 order on **means**: B > T > P.  
\(F^{\rm rel}\) order on means is **not** B < T < P (T is deepest). The v2 class rule was not a Forman partition.

## Rank tests (n=9)

| pair | Spearman ρ | p |
|------|------------|---|
| \(F^{\rm rel}\) vs dW8 | **−0.50** | **0.17** |
| v2-kind vs dW8 | −0.47 | 0.20 |
| v2-kind vs \(F^{\rm rel}\) | +0.22 | 0.56 |

Same honesty as v2 on this grid: \(R_{\rm mid}\) vs ΔW was ρ=+0.48, p=0.19. Directional, **not significant at n=9**.

The tight ρ=−0.976 in v2 `Mediator_Frel_vs_Ollivier.md` was an **8-point transition-densified slice**, not this full 3×3.

## Protocol call

| Test | On this 3×3 |
|------|-------------|
| Residual gate | PASS |
| S1.1 using v2 B/T/P labels | **not a clean ordered split** |
| S1.2 \(F^{\rm rel}\) mediates dW8 | **directional only** (p=0.17) |
| S1.2 dW8 means B > T > P | holds |

Do not upgrade the 3×3 to the same claim strength as the 3-archetype slice in note 32 or the 8-point mediator slice in v2.

## Still locked
SPARC lattice, Stage 2 cosmology, Ollivier agreement, continuum Ricci.

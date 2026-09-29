# Higher-simplex Forman + distance optimization methods

**Date:** 2026-09-29  
**Artifact:** `data/higher_forman_and_ot.json`

## 1. Forman on higher simplices

For a d-simplex α in a simplicial / CW complex:

```
F(α) = |{β^{d+1} ⊃ α}| + |{γ^{d−1} ⊂ α}| − |{parallel d-neighbors}|
```

Parallel neighbors = other d-simplices that share a (d−1)-face with α but do **not** share a common (d+1)-coface.

| d | Object | Role for bridges |
|---|--------|------------------|
| 0 | vertices | F_0 ≡ 0 (Forman) |
| 1 | edges | Standard Forman–Ricci; primary R_1 mediator |
| 2 | triangles | Face cohesion on mid-span clique complex |
| 3 | tetrahedra | Dense mid only (B-like); rare on sparse P |

**Synthetic bridge results (this session):**

| Identity | R_1 (edge) | n_2 (triangles) | n_3 | F_2 mid cells |
|----------|------------|-----------------|-----|---------------|
| B | −1.63 ± 0.20 | 17.7 | 11.6 | 17.7 |
| T | −0.31 ± 0.51 | 4.5 | 0.8 | 4.5 |
| P | +0.09 ± 0.28 | 0.8 | 0.0 | 0.8 |

R_2 on these small tubes was ~0 (mid F_2 ≈ bulk F_2 when almost all triangles sit in mid). **Interpretation:** higher Forman becomes informative when the complex has structure *outside* the mid-span (abutment faces, multi-tube, residual-clean defect graphs). On pure mid-dense tubes, **R_1 remains the separator**; n_2 and n_3 count as secondary diagnostics (B builds faces, P does not).

**Assert for Stream 1:** primary pass/fail uses R_1; report n_2, n_3, mean F_2 on mid faces as secondary; only promote R_2 if mid vs bulk triangle sets differ.

## 2. Distance optimization methods (for Ollivier W_1)

Ollivier κ needs W_1(m_x, m_y). Ways to compute / assert it:

| Method | Accuracy | Cost | Use when |
|--------|----------|------|----------|
| **Exact LP** (network simplex / HiGHS linprog) | Exact | O(poly) per edge; heavy | Small graphs, gold standard |
| **Sinkhorn / entropic OT** | Approximate (ε) | Matrix scaling; much faster | Medium graphs; Ricci flow literature uses ε~0.1 |
| **Beckmann / flow formulation** | Exact W_1 on graphs | Sparse flow LP | Graph geodesic ground metric |
| **Hungarian / assignment** | Exact if equal atoms | n³ | Equal-support discrete measures |

**Toy check (this session):** W_exact_LP = 1.0; Sinkhorn ε=0.05 → 0.999; ε=0.5 still ~1.0 on that instance.

**Assert protocol for Ollivier cross-check:**
1. Gold: LP W_1 on a subsample of edges (or full if N small).
2. Production: Sinkhorn with ε ∈ {0.05, 0.1}; require |κ_Sinkhorn − κ_LP| < δ on the subsample (e.g. δ = 0.05).
3. If Sinkhorn fails the assert, do not use R_O for pass/fail — fall back to R_F only.

## 3. How this plugs into streams

- Stream 1 mediator = **R_1** (Forman edge relative depth), optional R_O if Sinkhorn assert passes, optional higher-face counts.
- Stream 2 unchanged (SPARC estimators); no OT required.

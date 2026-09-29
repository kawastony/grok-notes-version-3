# Forman on simplicial complexes + Ollivier–Ricci

**Date:** 2026-09-29  
**Artifacts:** `data/forman_vs_ollivier.json`, prior Forman hysteresis JSON

## Forman on cell / simplicial complexes

Forman (2003, *Bochner’s Method for Cell Complexes*):

For each dimension p, curvature F_p assigns a number to each p-cell from its neighbors only.

**General (quasi-convex CW):**

F(α) = #{(p+1)-cells β > α} + #{(p−1)-cells γ < α} − #{parallel neighbors of α}

- **Parallel neighbors:** same dimension, share a face but not a coface (or the dual condition).
- **p = 1 (edges):** reduces to the familiar graph Forman–Ricci (degree + triangle corrections).
- **Higher d:** on the clique complex / Vietoris–Rips, F_d uses cofaces, faces, and parallel d-simplices.

Positive F everywhere ⇒ topological constraints (combinatorial Bochner): e.g. vanishing homology in that degree under suitable hypotheses.

**Simplicial formula (common network form):**

F(α) = |H_α| + (d+1) − |P_α|

where H_α = (d+1)-faces containing α, P_α = parallel neighbors.

**Why it matters for us:** bridge mid-span can be scored at edge level (d=1) and at triangle level (d=2) on the clique complex of the defect graph. Higher Forman sees cohesive faces the 1-skeleton only partially encodes.

## Ollivier–Ricci (coarse Ricci)

Transportation definition on a metric measure space:

κ(x,y) = 1 − W_1(m_x, m_y) / d(x,y)

On graphs, with idleness α ∈ [0,1]:

m_x^α(x) = α,  m_x^α(y) = (1−α)/deg(x) for y ∼ x

κ_α(x,y) = 1 − W_1(m_x^α, m_y^α) / d(x,y)

Lin–Lu–Yau: limit α → 1 of κ_α / (1−α).

**Meaning:** positive κ → neighborhoods overlap / transport is cheap (clustering, coherence). Negative κ → neighborhoods spread apart (tree-like branching).

W_1 is the 1-Wasserstein (Earth Mover) distance — optimal transport cost with ground metric = graph distance.

## Forman vs Ollivier (literature)

| Aspect | Forman | Ollivier |
|--------|--------|----------|
| Origin | Discrete Bochner / Laplacian | Coarse Ricci via optimal transport |
| Cost | O(edges × local stars) — fast | LP per edge — expensive |
| Emphasizes | Dispersal, combinatorial topology | Clustering, diffusion coherence |
| Weights | Natural as lengths / capacities | Natural as probabilities |
| Empirics | Often highly correlated with ORC on many networks; AFRC augmentations close the gap for community tasks |

Samal et al. (Sci Rep 2018): high correlation in many model and real networks; Forman usable as a fast proxy when coarse analysis suffices.

## Numerical comparison on our bridge tubes

Same B/T/P synthetic tubes as stream A. Relative depth R = −(mid − bulk) for both.

| Identity | R_Forman | R_Ollivier (α=0) |
|----------|----------|------------------|
| B | −1.14 ± 0.41 | −0.22 ± 0.04 |
| T | −0.53 ± 0.38 | −0.17 ± 0.04 |
| P | +0.24 ± 0.16 | −0.02 ± 0.05 |

**Global corr(R_F, R_O) ≈ 0.92** on these graphs. Within-identity corr is highest for B (≈0.996) and lower for P (sparser, noisier transport).

Both order B ≺ T ≺ P in relative depth (B deepest). Scales differ: Forman has larger dynamic range on these dense mid chords.

## Operational choice for the program

1. **Default micro mediator:** Forman relative depth R_F (fast, matches discrete Morse / Bochner language already in the constitution).
2. **Cross-check:** Ollivier relative depth R_O on the same residual-clean graphs when N is small enough for W_1.
3. **Higher Forman F_2** on mid triangles when the clique complex is non-trivial — tests whether face-level cohesion agrees with edge-level R.
4. Do not treat correlation as identity: Forman can miss transport-overlap structure that Ollivier sees (and conversely).

## Stream 1 status

Residual-clean **user** Forman graphs still not in-session. Synthetic bridge results + F vs O comparison are the stand-in until those dumps are available.

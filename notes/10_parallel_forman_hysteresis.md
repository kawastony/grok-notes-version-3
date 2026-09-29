# Parallel stream A — Forman–Ricci relative depth + hysteresis

**Date:** 2026-09-29  
**Artifact:** `data/forman_relative_depth_hysteresis.json`

## Convention (locked for this stream)

Forman–Ricci on edge e=uv (unweighted):

κ_F(e) = 4 − deg(u) − deg(v) + 3·#(triangles on e)

Relative raw depth:

R_raw = F_mid − F_all

Operational R for 3-bridge membership (so dense mid = active-capable deep well):

**R = −R_raw**

| Identity | dens mid chords | R mean | F_mid mean | gain mean | slope mean |
|----------|-----------------|--------|------------|-----------|------------|
| B (active-like) | 0.90 | **−1.14** | +3.34 | 0.87 | 0.020 |
| T (transitional) | 0.40 | **−0.43** | +0.89 | 0.74 | 0.008 |
| P (hollow/stall) | 0.08 | **+0.16** | +0.02 | 0.83 | 0.001 |

Spearman(identity B→T→P, slope) = **−0.85** (p ≈ 0)  
Spearman(R, slope) = **−0.98** (p ≈ 0)

Identity → relative Forman depth → early slope is numerically tight on these synthetic tubes.

## Hysteresis path B→T→P→T→B

Membership rules: R_leave = −0.55, R_return = −0.75, α proxy = gain.

| Segment | Behavior |
|---------|----------|
| B block | b=0 (active); R ≈ −0.95 |
| T worsen | leaves to b=1 then b=2 |
| P block | stuck b=2 (stall) |
| T improve | climbs to b=1 |
| B recover | returns b=0 only when R ≈ −0.95 |

**Observed:** leave R ≈ −0.15, return R ≈ −0.95, **width ≈ 0.79**

Hysteresis is present under the asymmetric R thresholds once the graph geometry is Forman-scored.

## What this is / is not

- **Is:** residual-free micro demonstration that relative Forman depth separates B/T/P and that membership hysteresis appears with the same thresholds as the abstract toy.
- **Is not:** residual-clean proof on the user’s real Forman defect graphs; not a derivation of galactic r_p.

## Next micro step

Replace synthetic tubes with residual-clean Forman graphs from the existing identity runs; recompute R = −(F_mid−F_all); test slope–R Spearman and worsen/improve hysteresis on real controls.

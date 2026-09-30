# Stream 1 synthetic Forman results

## Aggregate (5 seeds × B/T/P)

| kind | R0 mean | R0 std | dR8 mean | dW8 mean |
|------|---------|--------|----------|----------|
| B | 1.088 | 0.373 | +0.636 | **1.679** |
| T | 1.107 | 0.559 | −0.229 | 0.557 |
| P | **1.864** | 0.462 | −0.282 | 0.414 |

R0 order (low→high): **B ≈ T < P**

## Interpretation

1. **Relative depth R0**: Pause archetype P sits clearly above B/T. B and T overlap on R0 with this graph recipe (T mid not sparse enough vs B).
2. **Ricci-flow mid response dW8**: Strong ordering **B ≫ T > P**. Dense/active mid amplifies weight under dw/dt = −(F−F̄)w; pause mid stays comparatively inert.
3. **dR8**: B drifts up; P/T drift down — flow pushes archetypes apart in R-space.

## Programmatic use

- Primary discriminator for active vs pause under dynamics: **dW8** (or path integrated ΔW).
- Static classifier: **R0** works for P vs {B,T}; refine T mid sparsity if three-way static separation is required.
- Hysteresis thresholds can sit on R with leave/return asymmetry once T is stiffened.

## Artifact
`/content/stream1_synth_forman.csv`

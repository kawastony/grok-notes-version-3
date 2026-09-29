# Discrete Ricci flow dynamics + Ollivier metrics

**Date:** 2026-09-29  
**Sources:** Ni et al. Sci Rep 2019; Ollivier; v2 notes `Forman_curvature_dynamics.md`, `Forman_flow_dynamics_identity.md`, `Curvature_evolution_and_Ricci.md`

## 1. Discrete Ricci flow (architectural idea)

Continuum (Hamilton):

∂_t g_ij = −2 Ric_ij

Discrete on weighted graphs (Ollivier / Ni et al.):

w^{k+1}_ij = (1 − κ^k_ij) · d^k(i,j)

or continuous-time form:

d/dt d_ij(t) = −κ_ij(t) · d_ij(t)

**Effect:** positively curved edges shrink; negatively curved edges stretch. After iterations, inter-community edges become long → **surgery** (cut heavy edges) reveals communities.

## 2. Forman flow used in your v2 lattice program

Normalized discrete Forman flow on edge weights (from v2):

dw_e / dt = −(F(e) − F̄) w_e

| Condition | Effect |
|-----------|--------|
| F(e) < F̄ (more negative than mean) | dw > 0 → weight **increases** |
| F(e) > F̄ | weight decreases |

Relative mid curvature:

F^rel_mid := F_mid − F̄

When F^rel_mid < 0, mid sits in the **gain sector**. On residual-clean soft-mode tubes (v2):

| Identity | F^rel(0) | gain-sector frac | ΔW_8 |
|----------|----------|------------------|------|
| B baseline | **−0.84** | **0.66** | **+0.088** |
| T | −0.55 | 0.52 | +0.033 |
| P stall | **−0.33** | **0.46** | **+0.001** |

Correlation (F^rel, ΔW_8) ≈ **−0.997** on archetypes.

**Early window only** (steps ≲ 10–15). Late blow-up is numerical, not physics.

**Honesty:** graph Forman flow ≠ continuum Ricci / Einstein. Same *architecture* (curvature drives weight change), different object.

## 3. Ollivier curvature metrics (detail)

κ_α(u,v) = 1 − W_1(m_u^α, m_v^α) / d(u,v)

m_u^α(u) = α,  m_u^α(nbr) = (1−α)/deg(u)

| Metric | Meaning |
|--------|--------|
| κ > 0 | Neighborhoods overlap; transport cheap (cluster interior) |
| κ < 0 | Neighborhoods spread; tree-like / inter-community |
| κ ≈ 0 | Locally flat |

Lin–Lu–Yau: lim_{α→1} κ_α/(1−α).

**Cost:** exact OT per edge is expensive; Sinkhorn ε≈0.05–0.1 is the practical assert path (see notes/15).

**Role in program:** optional cross-check of Forman R / gain-sector; not required for Stream 1 pass if Forman flow already separates B/T/P.

## 4. Ricci flow + surgery (community detection)

1. Iterate discrete Ricci flow (Forman or Ollivier) 10–15 steps.  
2. Edges with large weight (stretched, inter-community) → cut (surgery).  
3. Connected components = communities.

Forman flow is the practical large-graph choice; Ollivier often higher quality, slower.

## 5. Link to 3-bridge / pause model

| Flow object | Bridge model |
|-------------|--------------|
| F^rel_mid deep | Active A — fast feed |
| F^rel_mid shallow | Pause P — stall |
| Early slope ∂_t W_mid | Intensity of active phase |
| Surgery / reweight | Pause transfer (reattach membership) |

Same flow law; identity sets relative curvature position; relative curvature sets trajectory.

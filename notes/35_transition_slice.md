# Transition-slice scan (Fix 2)

**Date:** 2026-10-01  
**Artifact:** `data/stream1_L10_transition_slice.json`

## Pre-registered (written before the loop)

- Axis: \(v_2=2.0\) fixed, \(v_1\in\mathrm{linspace}(1.65,2.35,13)\), L=10, d=3, mode 0, gate \(r_{\rm rel}\le10^{-6}\).
- Primary: Spearman(\(F^{\rm rel}\), dW8). Pass if \(\rho<-0.5\) and \(p<0.05\).
- Secondary: Spearman(\(v_1\), dW8). Expect \(\rho>0\).
- Axis labels only: P if \(v_1\le1.80\), T if \(1.80<v_1<2.15\), B if \(v_1\ge2.15\). Not a new ontology.

## Result
13/13 gated.

| test | ρ | p | call |
|------|---|---|------|
| **primary** \(F^{\rm rel}\) vs dW8 | **−0.714** | **0.0061** | **PASS** |
| secondary \(v_1\) vs dW8 | +0.588 | 0.035 | pass |
| axis-kind vs dW8 | −0.517 | 0.071 | miss (p>0.05) |

Mean dW8: P **−0.005**, T +0.010, B +0.009. P is the stall. B vs T on this axis is **not** cleanly ordered — T sits in the deep-well band. That is the same label issue as note 33.

## What this unlocks
On the **imbalance / transition slice**, relative Forman mediates early feed at n=13 with a pre-registered pass. This is the “special pieces” claim, not a full-landscape B>T>P theorem.

v2’s ρ=−0.976 on 8 points was the same region, tighter because it was hand-sliced. This scan is the honest densification of that path.

## Still not
Full-grid arrival, SPARC lattice, Ollivier, GR. Do not move the class cuts after seeing dW8.

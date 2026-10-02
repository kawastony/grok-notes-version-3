# L=10 baseline and L=12 matching test

**Date:** 2026-10-02  
**Artifact:** `data/stream1_L10_L12_match.json`  
**Protocol:** \(r=1\), gate \(10^{-6}\), \(v_1=2\), \(d=3\), anchors \(v_2\in\{1.8,2.0,2.2\}\).

## Pre-registered bar
The L=10 center window transfers if L=12 also has the most negative \(F^{\rm rel}\) and the largest early feed at \(v_2=2\), not at the edges.

## L=10
All gated.

| \(v_2\) | \(F^{\rm rel}\) | dW |
|--------|-----------------|-----|
| 1.8 | −0.72 | +0.0027 |
| 2.0 | **−0.92** | **+0.0168** |
| 2.2 | −0.69 | +0.0095 |

Center is the deepest and the strongest feed. L=10 baseline holds.

## L=12
All gated.

| \(v_2\) | \(F^{\rm rel}\) | dW |
|--------|-----------------|-----|
| 1.8 | **−1.07** | **+0.0112** |
| 2.0 | −0.64 | +0.0015 |
| 2.2 | −0.49 | +0.0021 |

Deepest curvature and strongest feed move to the low edge. Center feed collapses.

## Call
**Matching test fails.** The patchy window around \(v_2=2\) is an L=10 fact, not yet a volume-stable fact. Do not promote it to the QM side on this evidence. Tube edge count stayed 297 because the pair separation was held at \(d=3\); this is not a larger-tube test, only a larger bulk.

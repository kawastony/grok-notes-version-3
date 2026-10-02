# Midpoint/endpoint tool vs the hysteresis miss

**Date:** 2026-10-02  
**v2 source:** `L10_midpoint_endpoint_diagnostics.md`  
**Artifact:** `data/stream1_L10_midpoint_K.json`

## Was it used in note 40?
No. The hysteresis protocol was a carried-weight loop on \(\Delta W\) sign. It did not compute tilt or midpoint curvature.

## What the tool actually is
Finite-difference language on the pair density, not a calculus identity imposed on the flow:

\[
D_1=\frac{P_2-P_1}{P_1+P_2},\quad
K=\frac{2M-(P_1+P_2)}{P_1+P_2+2M}
\]

\(K>0\): midpoint excess over the average of the two ends. \(K<0\): end-heavy / hollow mid. v2 reading: boost keeps midpoint support; weaken makes \(K\) negative (\(-0.16\) on the −15% case) while \(|D_1|\) grows.

That is what “couldn’t be seen” in a single \(\Delta W\): tilt and hollowing are different failures.

## Applicability here
High, as a **diagnostic**, not as a fix for the solver blow-up.

Note 40 failed because carried Forman weights stayed in the feed state until the flow went unstable. \(K\) asks a prior question: did the **density** already hollow before the weights failed?

## This cut (\(v_2=2.0\), 7 points, all gated)

| \(v_1\) | \(D_1\) | \(K\) | \(M\) |
|--------|---------|-------|-------|
| 1.7 | +0.29 | +0.12 | 0.061 |
| 1.8 | +0.17 | +0.35 | 0.093 |
| 1.9 | −0.09 | +0.29 | 0.053 |
| 2.0 | −0.18 | +0.34 | 0.073 |
| 2.1 | +0.17 | +0.27 | 0.065 |
| 2.2 | +0.18 | +0.26 | 0.061 |
| 2.3 | +0.03 | +0.07 | 0.076 |

\(K\) stays **positive** on this imbalance scan. The midpoint is not the v2 weaken state (\(K=-0.16\)). Tilt \(D_1\) does move. So the loop never left “feed” for a geometric reason: this \(v_1\) path at \(v_2=2\) does not hollow the mid the way the −15% archetype did.

## Consequence
Do not rerun carried-weight hysteresis until a control actually drives \(K\) through zero. The −15% / polarized corner in v2 is the candidate, not another \(v_1\) sweep inside the feed band.

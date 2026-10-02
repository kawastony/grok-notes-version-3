# Polarized-corner check: \(K\) does not cross zero

**Date:** 2026-10-02  
**Artifacts:** `data/stream1_K_weaken_scan.json`, `data/stream1_Kax_weaken.json`

## Status labels
- Geometry mediation (\(F^{\rm rel}\to\) dW8, patchy in \(v_2\)): **partial breakthrough**
- Pause memory on these tubes: **negative result** (note 40)
- “Hysteresis failed because the path never hollowed”: **partially supported**, and now tighter
- Full bridge/pause lock: **not a breakthrough**

## What was implemented
The next test was hysteresis **only if** a control drives midpoint curvature through zero. Precondition first.

Path: \(v_2=2.3\) fixed, \(v_1\) from 2.2 down to 0.6 (polarized / weaken corner). All points residual-gated.

Slab \(K\) (note 41 definition): minimum \(+0.15\) at \(v_1=0.8\). Never negative.

Axial finite difference (site density at the two cores vs the geometric mid):

| \(v_1\) | \(K_{\rm ax}\) | \(D_1\) |
|--------|----------------|---------|
| 2.2 | +0.52 | −0.14 |
| 1.7 | +0.69 | −0.01 |
| 1.4 | +0.70 | −0.51 |
| 1.0 | +0.21 | −0.64 |
| 0.6 | **+0.07** | **−0.84** |

Tilt becomes strongly end-heavy. Midpoint excess shrinks toward zero but **does not cross**. v2’s \(K=-0.16\) on the −15% case is **not reproduced** with either definition on mode 0.

## Call
Hysteresis loop **not run**. Running leave/return on a path that never meets the hollow precondition would repeat note 40.

Note 41’s clarification stands only in the weak form: the earlier \(v_1\) sweep did not hollow. The stronger form — “go to the polarized corner and \(K\) will cross” — **fails** in this reconstruction. Pause memory stays unlicensed. Do not retune \(M\) until \(K\) looks negative.

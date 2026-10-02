# Equal interval, tilt, Wilson \(r\)

**Date:** 2026-10-02  
**Artifact:** `data/stream1_wilson_r_tilt.json`

## Equal interval
The feed window in \(v_2\) is approximately symmetric about 2.0: onset between 1.80 and 1.85, exit between 2.15 and 2.20. That is an equal interval of about 0.15–0.20 on each side. The miss at 1.95 means it is **not** a clean two-phase split. Tilt \(D_1\) is the candidate phase coordinate: it changes sign across that window while \(v_1\)-only sweeps do not hollow \(K\).

## Wilson scan
\(v_1=2\), \(d=3\), \(m_0=0.3\), \(r\in\{0.5,0.75,1.0,1.25,1.5\}\), \(v_2\in\{1.8,2.0,2.2\}\). All 15 points gated.

| \(r\) | \(K\) at 1.8 / 2.0 / 2.2 | \(D_1\) at 2.0 |
|------|--------------------------|----------------|
| 0.5 | −0.85 / −0.95 / −0.89 | +0.46 |
| 0.75 | +0.43 / +0.28 / +0.00 | +0.58 |
| 1.0 | −0.05 / −0.20 / +0.49 | +0.93 |
| **1.25** | **−0.47 / +0.17 / +0.51** | **−0.001** |
| 1.5 | −0.66 / +0.67 / +0.30 | +0.89 |

## Reading
- \(r=0.5\) hollows every cut. That is a collapsed midpoint, not a phase boundary. Do not use it as the pause phase.
- \(r=1.25\) is the equal-interval tuning: center untilted (\(D_1\approx 0\)), low edge hollow (\(K<0\)), high edge midpoint-excess (\(K>0\)). The two edges sit the same distance from \(v_2=2\).
- Standard \(r=1\) mixes the signs. The earlier hysteresis miss is partly a Wilson-point choice, not only a \(v_1\) choice.

## Not claimed
This does not pass leave/return. It says the pause/active split, if it exists, should be looked for at \(r\approx 1.25\) along \(v_2\), with tilt as the coordinate, not at \(r=1\) along \(v_1\).

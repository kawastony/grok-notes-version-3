# Cross-\(r\) stability of the structural point

**Date:** 2026-10-02  
**Artifact:** `data/stream1_r_stability.json`

## Pre-registered bar
At fixed \(v_1=2\), \(d=3\), residual-gated mode 0. A Wilson point passes only if

\[
|D_1(v_2=2)|<0.15,\quad K(1.8)<0,\quad K(2.2)>0.
\]

Regime claim needs a consecutive interval of such \(r\), not a single hit.

## Result
21/21 gated. Passes: **\(r=1.25\)** and **\(r=1.35\)** only. Not consecutive. Neighbours fail.

| \(r\) | \(D_1(2)\) | \(K(1.8)\) | \(K(2.2)\) | dW 1.8 / 2.0 / 2.2 | call |
|------|------------|------------|------------|---------------------|------|
| 1.10 | −0.90 | −0.23 | +0.51 | +0.004 / +0.011 / +0.008 | miss (tilt) |
| 1.15 | +0.47 | +0.50 | +0.75 | +0.008 / +0.007 / +0.003 | miss |
| 1.20 | −0.53 | +0.57 | +0.41 | +0.011 / +0.013 / +0.006 | miss |
| **1.25** | **−0.001** | **−0.47** | **+0.51** | +0.022 / +0.019 / +0.009 | **pass** |
| 1.30 | −0.86 | −0.95 | −0.10 | +0.022 / +0.006 / +0.005 | miss |
| **1.35** | **+0.15** | **−0.16** | **+0.73** | +0.002 / +0.024 / +0.017 | **pass (edge of bar)** |
| 1.40 | +0.47 | +0.11 | +0.81 | +0.013 / +0.036 / +0.012 | miss |

## Call
**Knife-edge, not a stable regime.** The equal-interval reading is a tuned diagnostic point at \(r=1.25\), with a second isolated hit at 1.35 that sits on the tilt bar. Early feed stays positive at all three anchors, so feed does not carry the edge distinction. Geometry does, and only at those two \(r\) values.

Downgrade note 44 from “structural regime” to “tuned reading point.” Do not densify \(v_2\) at \(r=1.25\) as if the Wilson interval had passed.

# Band-edge refine + mediation

**Date:** 2026-10-01  
**Artifacts:** `data/stream1_L10_boundary_refine.json`, `data/stream1_mediation_pooled65.json`

## Confidence language
The 35+37 upgrade is real. A numeric “87%” is a judgment, not a measured posterior. Keep the licensed sentence from the plan; do not treat the percent as data.

## Band map (same prereg bar, 13/13 gated)

| \(v_2\) | ρ | p | call |
|--------|---|---|------|
| 1.80 | −0.26 | 0.39 | miss (note 37) |
| **1.85** | **−0.83** | 0.00045 | **pass** |
| 1.90 | −0.76 | 0.0027 | pass |
| **1.95** | −0.40 | 0.18 | **miss** |
| 2.00 | −0.71 | 0.006 | pass |
| **2.05** | **−0.70** | 0.008 | **pass** |
| 2.10 | −0.87 | 0.00012 | pass |
| **2.15** | **−0.80** | 0.00097 | **pass** |
| 2.20 | −0.36 | 0.22 | miss |

Onset sits between 1.80 and 1.85. Exit sits between 2.15 and 2.20. The band is **not** a filled interval: \(v_2=1.95\) misses at n=13. That is a hole, not something to smooth over. n=13 Spearman is noisy; pooled tests stay the load-bearing claim.

## Mediation on pooled n=65 (notes 35+37, pre-refine)

| model | \(R^2\) |
|-------|---------|
| \(F^{\rm rel}\) only | **0.439** |
| \(v_1\) only | 0.012 |
| labels only | 0.035 |
| \(F^{\rm rel}+v_1\) | 0.440 |
| \(F^{\rm rel}+\) labels | 0.445 |

Δ\(R^2\) adding \(v_1\) to \(F^{\rm rel}\): **0.0005**. Adding labels: **0.006**. Adding \(F^{\rm rel}\) to \(v_1\): **0.427**.

Partial Spearman: \(F^{\rm rel}|v_1\) vs dW8 still ρ=−0.64, p=8×10^{-9}. \(v_1|F^{\rm rel}\) vs dW8 ρ=0.04, p=0.76.

**\(F^{\rm rel}\) absorbs the others.** In this regime the well is the mediator; coupling and frozen B/T/P add almost nothing.

## Licensed / not
Licensed: bounded local law + geometry-first mediator in the tested band.  
Not licensed: global B>T>P, filled-interval phase diagram, continuum Ricci.  
“Real graphs” in the S1 sense are already the L=10 gated tubes; remaining lock is hysteresis on those tubes and larger n, not a return to synthetic-only.

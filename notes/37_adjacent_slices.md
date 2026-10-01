# Adjacent \(v_2\) cuts + well-depth vs labels

**Date:** 2026-10-01  
**Artifact:** `data/stream1_L10_adjacent_slices.json`  
**Bar:** same as note 35 — Spearman(\(F^{\rm rel}\), dW8) \(<-0.5\) and \(p<0.05\).  
**Gate:** 13/13 on every cut.

## Per-cut primary

| \(v_2\) | n | ρ(\(F^{\rm rel}\), dW8) | p | call | mean dW8 P / T / B |
|--------|---|-------------------------|---|------|---------------------|
| 1.8 | 13 | −0.258 | 0.39 | **MISS** | 0.0069 / 0.0034 / 0.0116 |
| 1.9 | 13 | **−0.758** | 0.0027 | **PASS** | 0.0025 / 0.0016 / 0.0057 |
| 2.0 (note 35) | 13 | **−0.714** | 0.0061 | **PASS** | P stall; T/B feed |
| 2.1 | 13 | **−0.868** | 0.00012 | **PASS** | 0.0039 / 0.0079 / 0.0019 |
| 2.2 | 13 | −0.363 | 0.22 | **MISS** | 0.0112 / 0.0140 / 0.0056 |

Local law on the **band** \(v_2\in\{1.9,2.0,2.1\}\). Edges \(1.8\) and \(2.2\) are boundaries: same operator, same gate, signal drops below the bar. Frozen P/T/B means do **not** stay B>T>P on the edge cuts.

## Step 2 — mediator competition (pooled n=65 = 4 cuts + centre)

| predictor | Spearman vs dW8 | p |
|-----------|-----------------|---|
| \(F^{\rm rel}\) | **−0.656** | **3×10^{-9}** |
| \(v_1\) | +0.11 | 0.38 |
| frozen axis labels | −0.11 | 0.38 |

Well-depth tertiles of \(F^{\rm rel}\) (cuts at −0.863, −0.697), frozen on the well not on dW8:

| bin | n | mean dW8 |
|-----|---|---------|
| deep | 22 | **+0.0117** |
| mid | 21 | +0.0069 |
| shallow | 22 | **+0.0005** |

Geometry wins. Coupling \(v_1\) and the old B/T knife do not.

## Claim level
A **local** feed law on the imbalance band around \(v_2=2\): deeper relative Forman well → stronger early mid feed. Not a landscape theorem. Edge cuts are the map’s boundary.

Still not GR, SPARC lattice, or Ollivier.

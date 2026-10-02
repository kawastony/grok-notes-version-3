# S1.4 hysteresis on residual-gated L=10 tubes

**Date:** 2026-10-02  
**Artifact:** `data/stream1_L10_hysteresis.json`

## Protocol
Substrate: same L=10 pair operator, residual gate, tube graph, weighted Forman.  
Control: \(v_1\) from 2.30 down to 1.70 then back up, at \(v_2\in\{2.0,2.1\}\) (inside the active window).  
Memory: edge weights **carried** across the morph (independent solves have no path dependence by construction).  
State: active if \(\Delta W\) over 3 clipped steps \(>0\), else pause.  
Pass: return \(v_1\) > leave \(v_1\), and no curvature blow-up.

## Result
**MISS** on both cuts.

| \(v_2\) | leave \(v_1\) | return \(v_1\) | call |
|--------|---------------|----------------|------|
| 2.0 | none (active until numerical fail at 1.90) | — | miss |
| 2.1 | 1.70 (last point, solver fail) | none | miss |

Downsweep stayed in the feed state across the window. The loop did not open.

An earlier unclipped carry blew up after four steps (\(F^{\rm rel}\) jumped to \(10^{7}\)). That matches v2 `Ricci_flow_dynamics_investigation.md`: discrete Forman flow on this all-negative tube is fragile past the early window. The blow-up leg is **not** a hysteresis pass.

## What this means
Mediator evidence (notes 35–38) does not automatically give pause memory. On these tubes, carried-weight Forman flow does not yet show leave > return.

Still open: a stabilized flow (stronger clip, gain-only rule from v2) or a different memory variable than raw \(\Delta W\) sign. Do not import the synthetic \(\lambda\) width 0.25 as if it were this substrate.

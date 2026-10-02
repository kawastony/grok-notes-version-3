# Four-mode subspace \(dS\) at L=10

**Date:** 2026-10-02  
**Artifact:** `data/stream1_G_procrustes_L10.json`  
**Decision:** continue to L=12 only if the v2 negative \(G\) is recovered in sign and roughly in magnitude. It is not. L=12 not run.

## Setup
\(r=1\), gate \(10^{-6}\), \(d=3\), \(v_1=2(1+s\varepsilon)\), \(\varepsilon=0.05\), \(s\in\{0,0.25,0.5,0.75,1\}\), four gated modes at every step. Subspace \(dS\) is the baseline-subtracted mean ball density. Procrustes \(\mathrm{Tr}(PQ)=\sum\sigma^2(V_i^\dagger V_j)\).

v2 target: \(G_{\rm subspace}=-0.176\), endpoint \(dS=-0.00882\).

## Result

| \(s\) | \(S_1\) | \(S_2\) | \(dS(S_2)\) | \(\mathrm{Tr}(PQ)\) to next |
|------|---------|---------|-------------|------------------------------|
| 0 | 0.0374 | 0.0379 | 0 | 1.49 |
| 0.25 | 0.0403 | 0.0375 | −0.0004 | 2.52 |
| 0.50 | 0.0427 | 0.0491 | +0.0112 | 1.83 |
| 0.75 | 0.0432 | 0.0515 | +0.0136 | 1.05 |
| 1 | 0.0338 | 0.0359 | −0.0020 | — |

\(G(S_2)=−0.040\). \(G(S_1-S_2)=−0.032\). \(G(S_2-S_1)=+0.032\).

## Proxy
The two-mode core-2 proxy in note 53 was \(G=+0.22\). The four-mode \(S_2\) change is \(−0.040\). They do not track. Proxy demoted.

## Call
Sign of the partner-core subspace change is negative, so the direction is not ruled out. Magnitude is about 4× smaller than v2’s −0.176, and \(dS\) is not monotonic (positive at mid-path). Procrustes overlaps sit at 1.0–2.5, below the v2 L=10 bottleneck 3.92. Not a reproduction. Stop. No L=12.

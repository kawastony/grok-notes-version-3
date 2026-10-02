# Eight-mode check at L=10

**Date:** 2026-10-02  
**Artifact:** `data/stream1_G_k8_L10.json`

## What v2 actually used
`G12_subspace_and_d5_scan.md`: **n_acc=4** at every \(s\). The 8 in the operator notes is the Dirac ⊗ isospin component count, not the subspace size. The G path was four residual-accepted soft modes.

## What was run anyway
Same path as note 54, \(k=8\) requested. All 8 passed the \(10^{-6}\) gate at every \(s\). The upper end of the multiplet sits at \(|\lambda|\approx 0.005\)–\(0.008\), outside the v2 soft window \(10^{-4}\)–\(10^{-3}\).

| \(s\) | n_acc | \(dS(S_2)\) |
|------|-------|-------------|
| 0.25 | 8 | +0.017 |
| 0.50 | 8 | +0.015 |
| 0.75 | 8 | +0.010 |
| 1.00 | 8 | +0.007 |

\(G(S_2)=+0.149\). v2 target \(-0.176\). Sign does not match. Four-mode result in note 54 was \(-0.040\). Adding the harder modes flips the sign.

## Call
Eight-mode average is not the v2 observable. Do not continue to L=12 on it.

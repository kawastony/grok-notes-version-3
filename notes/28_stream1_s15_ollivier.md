# Stream 1 S1.5 — Ollivier cross-check

**Date:** 2026-10-01  
**Protocol:** `notes/16` S1.5  
**Artifact:** `data/stream1_s15_ollivier.json`

## Why this is a reconstruction
The 30 Colab files under `/content/data/stream1_real` were not present in this workspace or Drive. S1.5 was run on the **same B/T/P mid-density tube family** used for the Stream 1 helpers (10 seeds × 3 identities = 30 replicas): dense mid = B, intermediate = T, sparse mid = P.

If the Colab dumps differ in size or residual-clean cut, rerun this script on those edgelists before treating S1.5 as file-identical to S1.1–S1.4.

## Assert 1 — LP vs Sinkhorn
On mid-span edges (cap 12 per graph), \(\varepsilon=0.05\):

- edges compared: 329
- median \(|\kappa_{\mathrm{LP}}-\kappa_{\mathrm{Sinkhorn}}| \approx 10^{-8}\)
- **PASS** (threshold 0.05)

## Assert 2 — Forman vs Ollivier agreement

| Identity | \(F_{\mathrm{rel}}\) mean | Ollivier \(\kappa\) mid mean |
|----------|---------------------------|------------------------------|
| B | +1.688 | +0.674 |
| T | +0.031 | +0.230 |
| P | −0.263 | −0.038 |

- Spearman(\(F_{\mathrm{rel}}\), \(\kappa_O^{\mathrm{mid}}\)) = **0.903** (p ≈ 9e−12)
- Spearman(identity order B<T<P, \(\kappa_O^{\mathrm{mid}}\)) = **−0.943** (p ≈ 6e−15)

**PASS** (\(|\rho|>0.5\)). Ordering agrees: active mid is more clustered (higher Ollivier \(\kappa\)); pause mid is nearer zero / negative.

## Verdict
S1.5 **PASS** on this family: OT solver is not an artifact (LP ≈ Sinkhorn), and Ollivier tracks Forman relative structure.

This strengthens geometric robustness. It does not replace Forman as the default mediator (`notes/13`, `notes/15`).

## Still not claimed
Continuum Ricci, Einstein equation, SPARC lattice layer, Planck+DESI Stage 2.

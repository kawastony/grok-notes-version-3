# G-sign proxy, L=10 and L=12

**Date:** 2026-10-02  
**Artifact:** `data/stream1_G_sign_L10_L12.json`

## Setup
\(r=1\), gate \(10^{-6}\), \(d=3\), \(v_2=2\), \(v_1=2(1+s\varepsilon)\), \(\varepsilon=0.05\), \(s\in\{0,0.5,1\}\), two soft modes. Both volumes solved in this tree. This is not the Colab 4-mode Procrustes \(dS\).

Proxy: mean core-2 ball density over gated modes. \(G=(S_2(1)-S_2(0))/\varepsilon\).

## Result

| L | \(S_2(0)\) | \(S_2(1)\) | \(G\) | sign |
|---|------------|------------|-------|------|
| 10 | 0.0287 | 0.0398 | +0.222 | positive |
| 12 | 0.0217 | 0.0563 | +0.691 | positive |

Sign agrees across L=10 and L=12. It does **not** match v2’s \(G_{\rm subspace}\) (−0.176 at L=10, −0.045 at L=12). Different observable: core-2 density rose under a core-1 boost here; v2’s subspace \(dS\) fell.

## Call
Volume-stable sign on this proxy: yes. Reproduction of the v2 negative G: no. Do not quote +0.22 / +0.69 as the Colab number.

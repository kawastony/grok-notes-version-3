# v2 lookup: what “real Stream 1” actually is

**Date:** 2026-10-01  
**Repos:** `kawastony/grok-notes-version-2` vs Colab paste in this session.

## What v2 already ran (residual-clean operator)

Not chord-density toys. Soft-mode **density tubes** from the 8-component Wilson–Dirac + isospin hedgehog, L=10, d=3, residual gate \(r_{\rm rel}\sim10^{-14}\).

Primary notes:

- `Forman_curvature_dynamics.md`
- `Forman_flow_dynamics_identity.md`
- `Forman_flow_trajectories.md`
- `Mediator_Frel_vs_Ollivier.md`
- `Identity_propagation_3x3_results.md` (9-point \(v_1,v_2\) grid, all residual-clean)

Identity labels on the 3×3 grid are **B / T / P from \((R_{\rm mid}, P, H)\)**, not from mid-chord density.

| v2 archetype | \(F^{\rm rel}_{\rm mid}\) | early \(\Delta W_8\) |
|--------------|---------------------------|----------------------|
| Baseline B (2,2) | **−0.84** | **+0.088** |
| T / boost-like | ~ −0.55 | +0.03–0.05 |
| Polarized P (1.7,2) | **−0.33** | **~0** |

All-negative tube: \(F_{\rm mid}\sim-9\). Flow law same as v3: \(dw/dt=-(F-\bar F)w\), early window only.

Mediator test (8 residual-clean points): Spearman(\(F^{\rm rel}\), \(\Delta W\)) = **−0.976**. Ollivier mid sample ≈ **−0.005 constant** — **did not discriminate**. v2 conclusion: do not claim multi-Ricci agreement on that geometry.

## Colab “real” 30 replicas vs v2

| | v2 operator tubes | Colab `/content/data/stream1_real` |
|--|-------------------|-------------------------------------|
| \(R_0\) B / T / P | depth ~0.3–0.8 in \(F^{\rm rel}\) | 1.11 / 3.31 / 4.79 |
| dW8 B | **0.09** | **1.96** |
| geometry | soft-mode density, all-negative \(F\) | mid-chord B/T/P tubes (v3 synth family) |
| Ollivier | failed to split | v3 S1.5 pass on reconstructed tubes |

The Colab line “wrote 30 real graph replicas” is a **filename**. Numerically it is the **v3 synthetic / v2-tightened archetype family**, not the v2 Callias soft-mode graphs.

So S1.1 / S1.2 / S1.4 on that folder do **not** inherit v2’s residual-clean operator gate.

## What would actually unlock “real S1”

Export from the v2 Forman notebook, per \((v_1,v_2)\) point:

- edge list of the density-weighted tube  
- mid-edge mask  
- residual-clean flag  
- class B/T/P from the 3×3 rule  

Then rerun v3 S1.1–S1.5 **on those files**. Expect dW8 of order **0.01–0.1**, not ~2. If Ollivier is flat again, that is a **v2 result**, not a fail of Forman.

## SPARC in the same paste (do not mix)

Broken parse first: Q≤2 = 49, \(\Sigma_{\rm ref}=83\), N=43, \(S=-0.054\), dNLL=0.07.  
**Discard.**

Good parse: Q≤2 = 163, \(\Sigma_{\rm ref}=319.76\), N=92, \(S=-0.1889\), dNLL=3.17, shuffle_p=0.867, bootstrap frac(\(S<0\))=0.999, PyMC \(S=-0.1897\).  
That is `notes/24`–`25` / `29`. Lattice still off.

## Freeze language
v2 already had the micro mechanism on **operator** graphs. v3 S1 on `stream1_real` is a **controlled archetype battery**. Do not merge them into one “real data pass.”

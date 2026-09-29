# Colab test instructions — Stream 1 and Stream 2

**Date:** 2026-09-29  
**Code:** `code/colab_stream1_forman_flow.py`, `code/colab_stream2_sparc_rp.py`  
**v2 hints:** `Forman_curvature_dynamics.md`, `Forman_flow_dynamics_identity.md`, `Curvature_evolution_and_Ricci.md`

---

## STREAM 1 (micro Forman flow)

### Preferred input
Residual-clean soft-mode density tube graphs from your lattice program (same family as v2 Forman runs), labeled B / T / P (or continuous identity parameters).

### Cells
1. Paste `colab_stream1_forman_flow.py` helpers.  
2. Load graphs → `edges`, `mid_edges` per identity.  
3. Compute `F_rel`, `gain` (S1.1).  
4. Run `forman_flow(..., steps=8, dt=0.02)` → ΔW_8, slope (S1.2, S1.4 path).  
5. Optional: subsample Ollivier with Sinkhorn assert (S1.5).

### Pass criteria (from notes/16)
| Test | Pass |
|------|------|
| S1.1 | B has more negative F_rel than P; ordered separation |
| S1.2 | Spearman correlating F_rel or identity with slope; |ρ| meaningful |
| S1.4 | Hysteresis width > 0 on worsen/improve path |
| Early window | Only steps ≤ 8–10 interpreted |

### If no real graphs
Call `run_stream1_synth()` — synthetic only; does **not** replace residual-clean soft-mode graphs (v2 all-negative tube geometry differs from dense-chord synth).

---

## STREAM 2 (SPARC r_p)

### Cells
1. Paste `colab_stream2_sparc_rp.py`.  
2. Ensure catalog CSV + Rotmod paths exist (prior freeze setup).  
3. Loop galaxies: crude / threshold / logistic.  
4. Coverage cut; M0/M1; shuffle 2000 perms.  
5. Fill results table.

### Pass criteria
| Test | Pass |
|------|------|
| S2.3 | ΔNLL > 0, S < 0 |
| S2.4 | shuffle_p > 0.05 |
| S2.5 | ≥2 estimators agree |

### Freeze
Lattice residual layer stays off unless S2.4 fails stably under S2.5.

---

## Report back
Paste:
1. Stream1: mean F_rel / gain / ΔW_8 / slope by identity + Spearman.  
2. Stream2: table estimator | N | S | ΔNLL | shuffle_p.

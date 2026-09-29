# Parallel execution status (2026-09-29)

Tried simultaneously:

| Stream | Status | Outcome |
|--------|--------|---------|
| A. Forman–Ricci relative depth + hysteresis on synthetic bridges | **Done** | B/T/P separated by R; slope–R Spearman −0.98; hysteresis width ≈ 0.79 |
| B. SPARC r_p robustness protocol + synthetic estimator stress | **Done** | Protocol locked; synthetic ranking crude > thr > log for that toy family |
| C. Residual-clean Forman on **user** graphs | **Blocked** | Needs user’s residual-clean Forman identity graph dumps in-session |
| D. Cosmology stage chains | **Deferred** | Domain order: micro hysteresis on real Forman before cosmology |

## Simultaneous takeaway

Micro geometry (Forman R) and meso measurement discipline (SPARC r_p protocol) can advance in parallel without coupling. Coupling is only allowed after residual-clean Forman hysteresis and after SPARC estimator stability both pass.

## Immediate next (still parallelizable)

1. Ingest residual-clean Forman graphs → recompute R, slope, hysteresis.  
2. On Colab: run protocol steps 3–8 on real SPARC with all three r_p estimators; report ΔNLL and shuffle_p side by side.

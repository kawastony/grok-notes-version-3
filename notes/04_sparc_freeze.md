# SPARC residual freeze (raw data first)

## Pipeline
- Table1 + Rotmod, Q≤2
- X = (SB_disk / Σ_ref)^{1/7}
- Threshold r_p estimator; coverage cut R_max > 1.2 r_p
- M0: constant μ_*; M1: μ_* + S X

## Locked empirical result (N≈111, threshold estimator)
- M1 preferred over M0 (ΔNLL ≈ 7.7; hierarchical LOO Δelpd ≈ 6.9; weight ≈ 1 on M1)
- S < 0 (higher X ↔ lower μ̂ / larger transition scale)
- Post-M1 residual correlation vs X: **white** (shuffle p ∼ 0.80)
- BTFR residuals vs X: **white** (shuffle p ∼ 0.30)
- Influential point: UGC07577 (Pareto k>1); leave-one-out S still negative

## Guardrail
Do **not** introduce lattice/Callias residual layers until residual structure rejects white noise.  
R_cone mean-offset fix (synthesis PDF) is compatible as normalization; velocity-trend residuals remain open under the same residual discipline.

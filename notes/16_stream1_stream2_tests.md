# Stream 1 and Stream 2 — concrete test batteries

**Date:** 2026-09-29

---

## STREAM 1 — Residual-clean Forman (micro)

### Goal
On residual-clean identity graphs (B / T / P or equivalent labels), show that relative Forman depth R_1 separates identities, predicts early slope, and exhibits hysteresis under worsen/improve controls.

### Inputs required
- Edge list (or adjacency) per graph, with identity/class label
- Optional: residual-clean flag already applied
- Optional: mid-span node/edge mask; if absent, use whole-graph bulk vs densest k-core or user-defined mid

### Test S1.1 — Separation
1. Compute Forman κ on every edge (d=1).
2. R_1 = −(F_mid − F_bulk) with agreed mid mask.
3. Report mean ± std of R_1 by identity.
4. **Pass:** ordered means B < T < P (or documented order) and pairwise Mann–Whitney / permutation p < 0.05 for B vs P.

### Test S1.2 — Slope mediation
1. Early slope proxy (gain-sector fraction × depth, or your established ∂_t W measure).
2. Spearman(R_1, slope) and Spearman(identity_order, slope).
3. **Pass:** |ρ(R_1, slope)| > 0.5 and same sign as synthetic (− for our convention).

### Test S1.3 — Higher simplices (secondary)
1. Build clique complex to d=2 (d=3 if feasible).
2. Count n_2, n_3; mean F_2 on mid faces.
3. **Report only** unless mid vs bulk F_2 differ; then optional R_2 same formula.
4. **Soft pass:** n_2(B) > n_2(T) > n_2(P).

### Test S1.4 — Hysteresis
1. Control path: identity or continuous knob worsen B→T→P then improve P→T→B (or continuous R path).
2. Membership via R_leave = −0.55, R_return = −0.75 (or re-calibrated quantiles on real R_1).
3. **Pass:** leave_R > return_R (width > 0) for high-α subsample; low-α remains trapped in P-like band.

### Test S1.5 — Ollivier cross-check (optional)
1. Subsample edges; κ_LP vs κ_Sinkhorn (ε=0.05, 0.1).
2. **Assert:** median |Δκ| < 0.05 on subsample.
3. If assert holds: R_O ordering agrees with R_1 (Spearman > 0.5).

### Deliverables
Table of R_1 by identity; Spearman table; hysteresis width; optional OT assert; JSON dump for notes.

### Blockers
No residual-clean graph files in-session → run on synthetic until dumps provided.

---

## STREAM 2 — SPARC r_p robustness (meso)

### Goal
Confirm M1 preference and residual-whiteness are stable across r_p estimators (crude / threshold / logistic interior).

### Inputs
- SPARC Table1 (19-col CDS) + Rotmod
- Q ≤ 2 catalog with X = (SB_disk/Σ_ref)^{1/7}
- Code: `code/sparc_rp_colab_protocol.py`

### Test S2.1 — Estimator inventory
For each galaxy: crude, threshold (0.2–0.8 R_max), logistic.  
**Report:** N_ok, fraction near_bound / fail per estimator.

### Test S2.2 — Coverage cut
R_max > 1.2 r_p.  
**Report:** N after cut per estimator.

### Test S2.3 — M0 vs M1
μ̂ = r_p / R_max (or consistent scale).  
**Pass (per estimator):** ΔNLL(M0−M1) > 0 and S < 0 with bootstrap/HDI excluding 0 preferred.

### Test S2.4 — Residual whiteness
C_ee(dX) + 2000-perm shuffle on M1 residuals.  
**Pass:** shuffle_p > 0.05 (white) for primary estimator; report all three.

### Test S2.5 — Concordance
**Pass:** at least two estimators agree on (M1 preferred + white residuals).  
If only one agrees, do not promote lattice residual layer; diagnose estimator.

### Test S2.6 — Pareto-k (optional Bayes)
Hierarchical LOO; flag k > 0.7; leave-one-out refit.  
**Report:** whether S remains < 0.

### Deliverables

| estimator | N | S | ΔNLL | shuffle_p | pass S2.3 | pass S2.4 |
|-----------|---|---|------|-----------|-----------|-----------|
| crude | | | | | | |
| threshold | | | | | | |
| logistic | | | | | | |

### Freeze rule
Lattice/Callias residual layer stays **off** unless S2.4 fails (structured residuals) **and** that failure is stable under S2.5.

---

## Parallel execution order
1. S2 on Colab (data already in hand).  
2. S1.1–S1.4 on synthetic now; S1 on real graphs when dumps arrive.  
3. S1.5 only if S1.1 passes and graphs are small enough for LP subsample.

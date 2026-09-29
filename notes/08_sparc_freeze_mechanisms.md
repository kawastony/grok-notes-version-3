# SPARC freeze mechanisms — deep note

**Date:** 2026-09-29  
**Scope:** Why the residual freeze holds and what mechanisms it does / does not support.

## 1. What SPARC established (literature)

SPARC (Lelli, McGaugh, Schombert 2016): 175 disks, 3.6μm stellar mass + HI gas + resolved rotation curves.

### Radial Acceleration Relation (RAR)

g_obs = V_obs²/R correlates tightly with g_bar from baryons over ~4 dex.  
Critical scale ~10⁻¹⁰ m s⁻². Observed scatter ≲ 0.13 dex, largely observational.  
Residuals of the mean RAR do **not** correlate strongly with global galaxy properties in the classic analyses (Lelli et al. 2017; McGaugh et al. 2016).

### Baryonic Tully–Fisher (BTFR)

M_bar ∝ V_f⁴ with small intrinsic scatter. Linked to the same acceleration scale.

### Implication

When baryons are measured, the rotation curve is largely determined (and conversely). DM contribution, if interpreted that way, is specified by the baryon distribution.

## 2. Our freeze protocol (raw SPARC first)

| Step | Choice | Why |
|------|--------|-----|
| Quality | Q ≤ 2 | Drop poorly constrained curves |
| Proxy | X = (SB_disk / Σ_ref)^{1/7} | One-dimensionful surface-density input |
| Transition scale | Threshold r_p (interior 0.2–0.8 R_max window) | Avoid bound-locking of logistic fits |
| Coverage | R_max > 1.2 r_p | Drop edge-dominated estimates |
| Models | M0: μ ~ N(μ_*, τ²); M1: μ ~ N(μ_* + S X, τ²) | Constant vs linear surface-density response |
| Residual test | C_ee(dX) + permutation shuffle | Whiteness after M1 |
| Bayes | Hierarchical LOO (PyMC + ArviZ) | Confirm ΔNLL with elpd |

## 3. Locked numbers (session)

- N ≈ 111 (threshold, coverage cut)
- M1 preferred: ΔNLL ≈ 7.7; LOO Δelpd ≈ 6.9; model weight ≈ 1 on M1
- S ≈ −0.34 (frequentist) / −0.34 (hierarchical posterior mean); HDI excludes 0
- Post-M1 C_ee vs X: max\|C\| small, shuffle p ≈ 0.80 → **white**
- BTFR residual C_ee vs X: shuffle p ≈ 0.30 → **white**
- Pareto-k outlier: UGC07577 (k > 1); leave-one-out S still negative

## 4. Mechanism reading (what the freeze means)

### Supported
1. **Surface-density dependence of the transition scale:** higher X ↔ lower μ̂ (larger characteristic radius). This is an active-phase response law at galaxy scale (M1).
2. **After that linear term, residuals are consistent with noise** in X and in log SB_disk. No evidence for a further structured residual layer tied to X.
3. **BTFR residuals also white vs X** — independent observable, same conclusion.

### Not supported (yet)
1. Lattice / Callias / soft-mode residual structure as the driver of SPARC scatter after M1.
2. Identifying r_p with a derived pause radius from static Einstein+TAFA alone (Storey A: static field → Kepler, no μ).
3. Elevating R_cone from a normalization success (mean offset fix) to a proof of micro residual physics.

## 5. Freeze as pause discipline

In the v3 phase language:

- **Active:** fit M1; intensity of the X-response is real.
- **Pause:** residual-whiteness test before changing membership of the “explanation bridge.”
- White residuals ⇒ **do not transfer** to a lattice-residual bridge.
- That is Law of Pause applied to inference: acceptance of a new bridge requires structure, not only a preferred mean model.

## 6. Relation to RAR literature

Classic RAR: residuals about the mean g_obs(g_bar) law are small and largely non-systematic in global properties.  
Our M1 is a **different axis**: dependence of a transition-scale estimator μ̂ on surface-density proxy X.  
Finding S ≠ 0 does not contradict RAR; it asks whether transition location shifts with X.  
Finding **white** post-M1 residuals aligns with the RAR spirit: once the main baryon-linked term is removed, little structured residual remains in that coordinate.

## 7. Guardrails going forward

1. Any new micro claim on SPARC must improve residual structure (reject white) under the same protocol.  
2. r_p estimator changes must re-run M0/M1 + shuffle before interpretation.  
3. Cosmology chains stay separate until stage-ordered micro → meso tests pass.

## 8. One-line freeze

M1 is real; post-M1 residuals in X are white; lattice residual layers stay off until that changes.

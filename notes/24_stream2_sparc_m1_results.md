# Stream 2 SPARC — fixed catalog results

## Catalog
- table1 19-col map with e_Vflat between Vflat and Q
- Q≤2 = 163, Sigma_ref = 319.76
- matched rotmod 163, ok_thr after edge cut **N = 92**
- r_p_frac mean 0.39, range 0.20–0.80 (interior)

## M0 vs M1
| Model | params | NLL |
|-------|--------|-----|
| M0 | μ*=0.394, τ=0.132 | −140.64 |
| M1 | μ*=0.573, S=−0.189, τ=0.127 | −143.81 |
| **dNLL** | | **3.17** |

corr(μ_hat, X) = −0.258

M1 preferred: higher surface-brightness proxy X → lower μ (larger fractional transition radius), same sign as prior good runs.

## Residual structure
max\|C_ee\| = 0.0007, **shuffle_p = 0.867**
→ residuals after linear X term consistent with **white noise**.

## Guardrail
Raw SPARC residual test does **not** demand lattice/micro layer yet. Population trend with X is real; no evidence of structured residual correlation in X after M1.

## Artifacts
`/content/sparc_catalog/sparc_stream2_M1_residuals.csv`

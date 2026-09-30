# Stream 2 — bootstrap + hierarchical Bayes

N = 92 (threshold r_p, Q≤2, coverage cut)

## Frequentist point
μ₀ = 0.5732, S = −0.1889, τ = 0.1271

## Bootstrap (2000 resamples)
| | 16% | 50% | 84% |
|---|-----|-----|-----|
| S | −0.250 | −0.186 | −0.125 |
| μ₀ | 0.508 | 0.570 | 0.636 |
| τ | 0.117 | 0.125 | 0.134 |

fraction(S < 0) = **0.999**

## Hierarchical Bayes (PyMC, 2 chains × 2000)
| param | mean | sd | HDI 3–97% | r_hat |
|-------|------|-----|-----------|-------|
| μ₀ | 0.574 | 0.073 | [0.441, 0.710] | 1.00 |
| S | **−0.190** | 0.075 | **[−0.328, −0.052]** | 1.00 |
| τ | 0.130 | 0.010 | [0.113, 0.150] | 1.00 |

HDI for S entirely negative → slope robust under hierarchical prior.

## LOO
M1 rank 0, weight 1.0; elpd_diff vs M0 ≈ 2.29 (M1 preferred). No Pareto warnings.

## Conclusion
Population μ–X anti-correlation is stable (bootstrap + Bayes). Residuals after M1 remain white (shuffle_p ≈ 0.87). Stream 2 freeze: keep M1 as baseline galactic phenomenology; do not attribute residual structure to micro/lattice until a non-white signal appears.

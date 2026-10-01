# Stream 2 PyMC / LOO repeat — 2026-10-01

**Claim level:** Repeat of `notes/25`. Does not turn lattice on.

## Sampler
PyMC 5.28.5, ArviZ 0.22.0, N = 92. Two chains, 0 divergences, \(\hat R \approx 1.002\).

## M1 posterior

| param | mean | sd | HDI 3–97% |
|-------|------|-----|-----------|
| \(\mu_0\) | 0.5739 | 0.0727 | [0.4411, 0.7095] |
| \(S\) | **−0.1897** | 0.0751 | **[−0.3279, −0.0517]** |
| \(\tau\) | 0.1303 | 0.0102 | [0.1128, 0.1502] |

HDI for \(S\) entirely negative.

## LOO
M1 rank 0, weight 1.0; elpd_diff vs M0 = **2.2936**; no Pareto warning.

## Freeze
Same as `notes/24` / `notes/25`: one-layer SPARC, lattice residual **off**.

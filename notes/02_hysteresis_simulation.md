# Hysteresis simulation (2026-09-29)

## Thresholds
- R_leave = -0.55 (shallower → leave A)
- R_return = -0.75 (must deepen past leave to recover A)
- α_P2 = 0.70

## Results

| α | R leave | R return | Width | Hysteresis | Note |
|------------|-------------|--------------|-------|------------|------|
| 0.20 | −0.55 | — | — | No | Trapped in P_2 |
| 0.50 | −0.55 | — | — | No | Trapped in P_2 |
| 0.75 | −0.55 | −0.76 | +0.21 | **Yes** | Recovery after deeper well |
| 0.90 | −0.55 | −0.76 | +0.21 | **Yes** | Same |

## Interpretation
- Asymmetric thresholds produce a real loop when α is high enough to avoid P_2.
- Low α: improving R alone does not restore A — acceptance is required.
- Falsifier on real data: no loop in residual-clean slope–R sweeps, or recovery independent of any α-proxy.

Data: `data/hysteresis_3bridge_toy.json`

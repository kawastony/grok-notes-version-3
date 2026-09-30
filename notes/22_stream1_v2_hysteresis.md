# Stream 1 v2 + hysteresis — success

## Tightened T (v2 archetypes)

| kind | R0 mean | dR8 | dW8 |
|------|---------|-----|-----|
| B | **0.399** | +0.388 | **1.226** |
| T | **2.095** | −0.930 | 0.544 |
| P | **2.921** | −0.833 | 0.427 |

**R0 order: B < T < P** (clean)
- ΔR0(T−B) = 1.696
- ΔR0(P−T) = 0.826

Static three-way separation achieved by longer mid tube, lower T/P mid weight, weaker side attach, no T chords.

Dynamic discriminator unchanged: dW8 B ≫ T > P.

## Hysteresis on R

From R0 means:
- R_leave = 1.247
- R_return = 0.778
- width_R = 0.470

Morph sweep λ: B→P
- λ_leave (upsweep active→pause) ≈ **0.30**
- λ_return (downsweep pause→active) ≈ **0.10**
- λ hysteresis width ≈ **0.20**

Loop is asymmetric: system stays in pause on the way down until R drops below R_return — classic hysteresis, not a single threshold.

## Artifacts
- `/content/stream1_synth_forman_v2.csv`
- `/content/stream1_hysteresis_up.csv` / `_down.csv`
- `/content/stream1_hysteresis_summary.json`

## Status vs program
Forman relative depth + discrete Ricci flow now give:
1. Identity-like labels (B/T/P) from geometry
2. Propagation-like response (dW8)
3. Path dependence (hysteresis) — minimal dynamical model of pause vs active without FTL claims

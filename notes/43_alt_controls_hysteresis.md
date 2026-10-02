# Alternative controls, then hysteresis

**Date:** 2026-10-02  
**Artifacts:** `data/stream1_alt_controls.json`, `data/stream1_hyst_m0.json`

## Scan (axial \(K\), all gated)

| tag | control | \(K_{\rm ax}\) | \(D_1\) |
|-----|---------|----------------|---------|
| close | \(d=1\) | −0.01 | −0.02 |
| far | \(d=5\) | +0.79 | 0 |
| far_imbal | \(d=6\), \(v=(1.7,2.3)\) | **−0.21** | −0.18 |
| narrow | \(w=0.4\) | +0.72 | +0.74 |
| wide | \(w=2.5\) | +0.35 | −0.62 |
| narrow_imbal | \(w=0.5\), \(v=(0.5,2.5)\) | **−0.07** | −0.88 |
| m0_0 | \(m_0=0\) | **−0.50** | −0.55 |
| m0_1 | \(m_0=1\) | +0.01 | −0.77 |
| r_half | \(r=0.5\) | **−0.95** | +0.46 |

\(v_1\) alone does not hollow. Separation, bare mass, and Wilson \(r\) do.

## Next test
Same lattice, \(v_1=v_2=2\), \(d=3\), sweep \(m_0\) from 0.30 to 0. \(K\) **does cross** (range −0.50 to +0.43), but not monotonically (negative at 0.30, 0.15, and 0.0).

Carried-weight loop, same pass bar as note 40: return control > leave control, no blow-up.

**MISS.** Downsweep stayed active across the whole \(m_0\) range, including \(K<0\) points. Upsweep failed numerically at \(m_0=0.15\). No leave/return pair.

## Call
Finding a hollow geometry is not enough. On this path, \(K<0\) and early feed coexist, and the carried Forman loop still does not open before it blows up. Pause memory remains unlicensed. \(r\) and \(d\) are real alternative controls; they were not used as the loop variable because \(d\) changes the tube and \(r=0.5\) is a discretization change, not an identity knob.

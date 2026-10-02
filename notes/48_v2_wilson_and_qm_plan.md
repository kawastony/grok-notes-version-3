# Why v2 never hit the Wilson-\(r\) irregularity, and when to connect to QM

**Date:** 2026-10-02

## What v2 did in this kind of situation
v2 treated Wilson \(r\) as a regulator, not a phase dial.

- Free 8-component Wilson spectrum was checked once, at \(r=1\), \(m=0.5\), \(L=4\): lowest gap matched the analytic dispersion exactly (0.500000), no spurious kernel, doublers lifted (`Eight_component_algebra_and_free_spectrum.md`).
- After that, \(r\) was frozen. Scans moved \(d\), \(v\), \(L\), residual gate \(10^{-6}\), not \(r\).
- When a surrogate looked suggestive but was not the operator (fractional form), it was demoted. When a 4-component embedding failed algebraically, it was ruled out. The discipline was: fix the healthy UV point, then vary identity parameters.
- Residual gating was the control against lattice artefacts. Chirality diagnostics were only computed after the gate.
- Laws were split into derived, ansatz, guiding, and extrapolated (`Framework_laws_derived_vs_guiding.md`). A numerical coincidence did not get promoted.

## Why this situation did not arise
The irregular \(D_1(r)\) table is what you get when you promote the regulator to a coordinate. v2 never asked \(r\) to organize phases. At the healthy point \(r=1\), doublers are lifted and the free gap matches. Off that point the Wilson term changes the explicit chiral breaking and the doubler lift, so soft-mode geometry can jump without a continuum meaning. Notes 46–47 are that jump. v2 avoided it by not scanning \(r\).

## QM connection plan
Do not connect the isolated \(r=1.25\) point to continuum QM. It failed the noise check.

Connect only through the residual-gated, \(r=1\) operator, and only for claims already derived in v2:

1. Keep \(r=1\), gate \(10^{-6}\), 8-component Wilson–Dirac. That is the QM object: a lattice Dirac operator in the Callias / Jackiw–Rossi class.
2. The already-earned QM link is the index: soft-mode count versus \(N_{\rm def}\) on single defects, after the gate. Not tilt, not Forman feed.
3. The standing micro claim (notes 35–38) is a lattice geometry fact: \(F^{\rm rel}\) mediates early feed in a patchy \(v_2\) window. It becomes a QM statement only if the same ordering survives at \(r=1\) under a larger \(L\) with the residual gate held. That is the matching test.
4. Pause memory, Wilson-regime language, and \(\langle\gamma_5\rangle\) as the phase variable stay off the QM side until a pre-registered test passes at the healthy point.

Until step 3, the QM connection is the v2 index statement, not the v3 \(r\) scan.

# L=15 / L=20 matching attempt

**Date:** 2026-10-02

## What was asked
Same bar as note 50: at \(r=1\), gate \(10^{-6}\), \(v_1=2\), \(d=3\), does the L=10 center peak (most negative \(F^{\rm rel}\), largest early feed at \(v_2=2\)) survive at L=15 and L=20?

## What ran
The operator at L=15 builds: \(N=27000\), nnz \(=377384\). The soft-mode solve (shift-invert) was killed, exit 137, on the first anchor \(v_2=2\). A joint L=15/L=20 run was killed the same way before any row was written. L=20 was not reached. \(N=64000\) would be heavier.

## Call
L=15 and L=20 are **not run**. No new pass or fail on the volume bar. The last completed match remains note 50: L=10 center peak, L=12 miss.

v2’s finite-size note already flagged residual Wilson / mass-scale artefacts that do not scale out cleanly at these small volumes. That is consistent with the L=12 move of the peak to the low edge. It is not a substitute for an L=15 number.

Next time this is run, it needs a machine that can hold the shift-invert factorization. Do not treat an unsolved L=20 as a scaling result.

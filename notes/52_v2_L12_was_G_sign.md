# Why v2 L=12 succeeded, and what that is not

**Date:** 2026-10-02

## How v2 did it
`G12_L12_residual_gated_path.md` (2026-09-26), executed on Colab, not in the sandbox.

- L=12, d=3, cores (6,6,5)/(6,6,8), N=13824
- Boost path \(v_1=v_0(1+s\varepsilon)\), \(\varepsilon=0.05\), \(s\in\{0,0.25,0.5,0.75,1\}\)
- eigsh shift-invert, residual gate
- Observable: subspace \(dS\), endpoint \(G=(dS(1)-dS(0))/\varepsilon\), Procrustes \(\mathrm{Tr}(PQ)\)

Sandbox attempt of the same volume check had already failed (`G12_L12_volume_check.md`, `Bottleneck_eigensolve_status.md`: exit 137). Matrix-free matvec worked through L=14. Soft eigenvalues did not, without high RAM.

## Why it counted as success
The locked claim was narrow:

- residual-gated soft multiplet resolved
- \(G_{\rm subspace}\) negative at L=10 (−0.176) and L=12 (−0.045)
- magnitude volume-dependent
- \(\mathrm{Tr}(PQ)\) continuity weaker than L=10; not a full-rank bottleneck claim

Success meant the **sign of the propagation response survived**. It did not mean a center feed window survived.

## What v3 ran instead
Note 50 used this sandbox, \(r=1\), three \(v_2\) anchors, and scored \(F^{\rm rel}\) and early feed. L=12 solved here. The center peak did not transfer. That is a different test, and a miss. The slides’ “L=12 attempts fail” line matches the sandbox bottleneck, not the Colab G12 sign result.

## Next, on the v2 path
Do not retry L=15/20 shift-invert here. The matching test v2 actually passed is the G sign. If a next run is done, it is that boost-path \(G\) at L=10 in this tree, compared with the published L=12 Colab number −0.045, not another feed-window scan at L=20.

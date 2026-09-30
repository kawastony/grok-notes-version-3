# Stream 2 SPARC — false start

## Observed (broken catalog)
- raw shape (175, 19) OK count
- Q≤2 = **49** (expect ~163)
- Sigma_ref = **83.34** (expect ~300–320)
- ok_thr N = 43
- corr(μ,X) ≈ −0.06 (expect ~−0.35)
- dNLL(M0−M1) = 0.07 (no signal)
- shuffle_p = 0.66 (white but underpowered / wrong X)

## Cause
Whitespace parse of CDS `table1.dat` shifts SB_disk / Q / Vflat. Quality cut and X proxy become meaningless.

## Fix
Inspect first lines; use fixed column positions from SPARC ReadMe or prior working 19-col map; verify:
- Q value_counts ~ 99/64/12 for Q=1/2/3
- SB_disk median ~ 300+
- Q≤2 ~ 163
Then re-run threshold r_p + M0/M1.

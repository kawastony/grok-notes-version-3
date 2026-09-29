# Stream 2 — SPARC r_p Colab protocol

**Date:** 2026-09-29  
**Code:** `code/sparc_rp_colab_protocol.py`

## What to run on Colab

1. Load Q≤2 catalog + Rotmod (same as freeze).
2. For each galaxy compute crude / threshold / logistic r_p + status flags.
3. Interior-only + coverage R_max > 1.2 r_p per estimator.
4. M0 vs M1 (lstsq NLL) per estimator.
5. C_ee(dX) + 2000-perm shuffle on M1 residuals per estimator.
6. Optional: hierarchical LOO + Pareto-k.
7. Report table:

| estimator | N | S | ΔNLL | shuffle_p |
|-----------|---|---|------|-----------|
| crude | | | | |
| threshold | | | | |
| logistic (interior) | | | | |

Freeze holds if M1 preferred and shuffle_p remains high (white) for the primary interior estimator(s).

Helpers in the repo implement rp_*, corr_vs_sep, m0_m1. Paste rotmod paths from your catalog.

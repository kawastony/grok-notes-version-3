# SPARC r_p robustness protocol — Colab-ready (steps 3–8)
# Assumes Table1 + Rotmod already loaded as in prior notebooks.
# Requires: pandas, numpy, scipy; optional pymc/arviz for LOO

import numpy as np
import pandas as pd

def rp_crude(r, V, frac=0.9):
    Vmax = np.max(V)
    hit = np.where(V >= frac * Vmax)[0]
    return float(r[hit[0]]) if len(hit) else float(r[-1])

def rp_threshold(r, V, lo=0.2, hi=0.8, target=0.75):
    Vmax = np.max(V)
    y = V / Vmax
    R_max = float(r[-1])
    mask = (r >= lo * R_max) & (r <= hi * R_max)
    if mask.sum() < 3:
        return None, "too_few"
    rr, yy = r[mask], y[mask]
    for i in range(len(yy) - 1):
        if yy[i] < target <= yy[i + 1]:
            t = (target - yy[i]) / (yy[i + 1] - yy[i] + 1e-12)
            rp = float(rr[i] + t * (rr[i + 1] - rr[i]))
            frac = rp / R_max
            if frac <= lo + 0.02 or frac >= hi - 0.02:
                return rp, "near_bound"
            return rp, "ok"
    return None, "no_cross"

def rp_logistic(r, V):
    from scipy.optimize import curve_fit
    Vmax = np.max(V)
    y = V / Vmax
    R_max = float(r[-1])
    def f(x, a, b):
        return 1.0 / (1.0 + np.exp(-(x - a) / (b + 1e-6)))
    try:
        popt, _ = curve_fit(
            f, r, y, p0=[0.4 * R_max, 0.2 * R_max],
            bounds=([0.15 * R_max, 0.01], [0.85 * R_max, R_max]),
            maxfev=5000,
        )
        a = float(popt[0])
        frac = a / R_max
        if abs(frac - 0.15) < 0.02 or abs(frac - 0.85) < 0.02:
            return a, "bound"
        return a, "ok"
    except Exception:
        return None, "fail"

def corr_vs_sep(values, coord, n_bins=8, n_perm=2000, seed=0):
    values = np.asarray(values, float) - np.mean(values)
    coord = np.asarray(coord, float)
    i, k = np.triu_indices(len(values), k=1)
    d = np.abs(coord[i] - coord[k])
    prod = values[i] * values[k]
    edges = np.linspace(d.min(), d.max() + 1e-12, n_bins + 1)
    C, counts = [], []
    for b in range(n_bins):
        m = (d >= edges[b]) & (d < edges[b + 1])
        counts.append(int(m.sum()))
        C.append(float(prod[m].mean()) if m.sum() else float("nan"))
    max_abs = float(np.nanmax(np.abs(C)))
    rng = np.random.default_rng(seed)
    null = []
    for _ in range(n_perm):
        sh = values.copy()
        rng.shuffle(sh)
        prod_s = sh[i] * sh[k]
        Cs = []
        for b in range(n_bins):
            m = (d >= edges[b]) & (d < edges[b + 1])
            Cs.append(float(prod_s[m].mean()) if m.sum() else 0.0)
        null.append(np.nanmax(np.abs(Cs)))
    p = float(np.mean(np.array(null) >= max_abs))
    return {"C": C, "counts": counts, "max_abs_C": max_abs, "shuffle_p": p}

def m0_m1(mu, X):
    mu = np.asarray(mu, float)
    X = np.asarray(X, float)
    mu0 = mu.mean()
    tau0 = mu.std(ddof=1)
    nll0 = 0.5 * len(mu) * np.log(2 * np.pi * tau0**2) + 0.5 * np.sum((mu - mu0) ** 2) / tau0**2
    A = np.column_stack([np.ones(len(X)), X])
    coef, _, _, _ = np.linalg.lstsq(A, mu, rcond=None)
    mu_star, S = coef
    resid = mu - A @ coef
    tau1 = resid.std(ddof=2)
    nll1 = 0.5 * len(mu) * np.log(2 * np.pi * tau1**2) + 0.5 * np.sum(resid**2) / tau1**2
    return {
        "M0": {"mu": float(mu0), "tau": float(tau0), "NLL": float(nll0)},
        "M1": {"mu_star": float(mu_star), "S": float(S), "tau": float(tau1), "NLL": float(nll1)},
        "dNLL": float(nll0 - nll1),
        "resid": resid,
    }

print("SPARC r_p protocol helpers loaded")

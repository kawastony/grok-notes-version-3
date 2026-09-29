# =============================================================================
# STREAM 1 — Forman relative curvature + discrete flow (Colab cells)
# Based on grok-notes-version-2: Forman_curvature_dynamics.md
# =============================================================================
# Paste cells top-to-bottom. Requires: numpy, scipy; optional networkx
# INPUT: residual-clean graphs as edge lists + identity labels
#   graphs = {"B": [(u,v),...], "T": [...], "P": [...]}  # or list of dicts
#   mid_mask optional: set of nodes defining mid-span
# =============================================================================

import numpy as np
from collections import defaultdict

# --- Cell 1: Forman κ and relative depth ---

def forman_edge_kappa(edges):
    """Unweighted combinatorial Forman on graph edges."""
    nbrs = defaultdict(set)
    for u, v in edges:
        nbrs[u].add(v); nbrs[v].add(u)
    tri = defaultdict(int)
    nodes = list(nbrs.keys())
    for u in nodes:
        for v in nbrs[u]:
            if v <= u: continue
            for w in nbrs[u] & nbrs[v]:
                if w > v:
                    for ee in [(u,v),(v,w),(u,w)]:
                        tri[tuple(sorted(ee))] += 1
    kappa = {}
    for u, v in edges:
        e = tuple(sorted((u, v)))
        kappa[e] = 4 - len(nbrs[u]) - len(nbrs[v]) + 3 * tri[e]
    return kappa

def relative_mid(kappa, mid_edges):
    F_all = np.mean(list(kappa.values())) if kappa else 0.0
    if not mid_edges:
        return 0.0, F_all, 0.0
    F_mid = np.mean([kappa[tuple(sorted(e))] for e in mid_edges])
    F_rel = F_mid - F_all
    gain = np.mean([1.0 if kappa[tuple(sorted(e))] < F_all else 0.0 for e in mid_edges])
    return float(F_rel), float(F_all), float(gain)

# --- Cell 2: discrete Forman flow (v2 law) ---
# dw/dt = -(F - Fbar) w ; early window only

def forman_flow(edges, mid_edges, steps=8, dt=0.02):
    edges = [tuple(sorted(e)) for e in edges]
    mid_edges = [tuple(sorted(e)) for e in mid_edges]
    weights = {e: 1.0 for e in edges}
    traj = []
    for step in range(steps + 1):
        kappa = forman_edge_kappa(edges)
        Fbar = float(np.mean(list(kappa.values())))
        F_rel, _, gain = relative_mid(kappa, mid_edges)
        W_mid = sum(weights[e] for e in mid_edges if e in weights)
        traj.append({"step": step, "W_mid": W_mid, "F_rel": F_rel, "gain": gain, "Fbar": Fbar})
        if step == steps:
            break
        new_w = {}
        for e, w in weights.items():
            F = kappa.get(e, Fbar)
            new_w[e] = max(w * (1.0 - dt * (F - Fbar)), 1e-8)
        s, s0 = sum(new_w.values()), sum(weights.values())
        weights = {e: v * s0 / s for e, v in new_w.items()}
    dW = traj[-1]["W_mid"] - traj[0]["W_mid"]
    return traj, float(dW), float(dW / steps)

# --- Cell 3: S1.1–S1.4 battery ---
# Example with synthetic tubes if real graphs not loaded:

def synth_bridge(identity, seed=0):
    rng = np.random.default_rng(seed)
    L, M, R = 3, 5, 3
    edges = []
    for i in range(L-1): edges.append((i, i+1))
    for i in range(R-1): edges.append((L+M+i, L+M+i+1))
    for i in range(M-1): edges.append((L+i, L+i+1))
    edges += [(L-1, L), (L+M-1, L+M)]
    dens = {"B": 0.9, "T": 0.4, "P": 0.1}[identity]
    for i in range(M):
        for j in range(i+2, M):
            if rng.random() < dens:
                edges.append((L+i, L+j))
    edges = list({tuple(sorted(e)) for e in edges})
    mid = set(range(L, L+M))
    mid_edges = [e for e in edges if e[0] in mid and e[1] in mid]
    return edges, mid_edges

def run_stream1_synth(n_seeds=8):
    rows = []
    for ident in ["B", "T", "P"]:
        for s in range(n_seeds):
            edges, mid = synth_bridge(ident, s)
            kappa = forman_edge_kappa(edges)
            F_rel, Fbar, gain = relative_mid(kappa, mid)
            traj, dW, slope = forman_flow(edges, mid, steps=8, dt=0.02)
            rows.append({"id": ident, "F_rel": F_rel, "gain": gain, "dW8": dW, "slope": slope})
    import pandas as pd
    df = pd.DataFrame(rows)
    print(df.groupby("id")[["F_rel", "gain", "dW8", "slope"]].mean())
    # S1.2 Spearman
    from scipy.stats import spearmanr
    order = {"B": 0, "T": 1, "P": 2}
    rho, p = spearmanr([order[r] for r in df["id"]], df["slope"])
    print(f"Spearman(identity, slope)={rho:.3f} p={p:.4f}")
    return df

print("Stream 1 helpers loaded. Call run_stream1_synth() or pass real graphs to forman_flow.")

# Forman discrete Morse theory — deep note

**Date:** 2026-09-29  
**Sources:** Forman 1998 (Adv. Math.), Forman discrete gradient notes, Saucan arXiv:2003.03844, Banchoff/Bloch connection.

## 1. Discrete Morse function

On a cell complex K, a function f assigning a real to every cell is a **discrete Morse function** if for each p-cell α:

- #{β^{p+1} > α | f(β) ≤ f(α)} ≤ 1
- #{γ^{p−1} < α | f(γ) ≥ f(α)} ≤ 1

Intuition: at most one “uphill” coface and at most one “downhill” face that violate the strict height order.

## 2. Critical cells

α is **critical** if both counts are zero:
- no coface with f(β) ≤ f(α)
- no face with f(γ) ≥ f(α)

Index of a critical cell = its dimension. Minima at vertices; maxima at top-dimensional cells (closed manifold case).

## 3. Discrete gradient vector field

A **discrete vector field** V is a collection of pairs {α < β} (α face of β, codim 1) with each cell in at most one pair.

V is a **gradient vector field** iff there are **no nontrivial closed V-paths**.

**Theorem (Forman):** V is the gradient of some discrete Morse function ⇔ no closed V-paths.

Critical cells of V = cells not in any pair.

## 4. Main structural theorem

K is simple-homotopy equivalent to a CW complex with exactly one p-cell per critical p-cell of V.

Homology of the Morse complex (critical cells + gradient-path incidence) equals homology of K.

## 5. Gradient paths and flow

A V-path: alternating sequence of paired and face relations.  
**No closed paths** ⇒ flow is acyclic ⇒ can define discrete “time” along the gradient.

This is the discrete analogue of −∇f flow. **Pause / stall** in our model language maps to **critical cells** or blocked pairings; **transfer** maps to allowing a new pairing (changing V).

## 6. Banchoff / Bloch / Forman link (Saucan)

- Banchoff: polyhedral Morse via height functions and combinatorial index at vertices (middle-vertex count).
- Bloch: Forman and Banchoff theories are essentially interchangeable in the relevant combinatorial setting.
- Saucan: curvature-based persistent homology via Banchoff/Forman; **defect curvature correlates strongly with Forman–Ricci** — explains empirical PH ↔ Forman-Ricci coincidence in network studies.

## 7. Forman–Ricci curvature (graph form)

For edge e=uv (unweighted schematic):

κ_F(e) = 4 − deg(u) − deg(v) + 3·#(triangles on e)

Negative κ_F ↔ tree-like branching (spread).  
Positive κ_F ↔ cliquey cycles (circulation).

Weighted Forman–Ricci generalizes with vertex/edge weights.

## 8. Relative depth as operational R

Absolute mid-span Forman curvature can look similar across identity classes.  
**Relative** depth

R = F_mid − F̄

(rank of the bridge vs the rest of the tube) is the mediator in the mechanism chain:

identity → R → gain-sector occupancy → early feed slope

Deep R (more negative well) → active bridge A.  
Shallow R → pause bridges P₁ / P₂.

## 9. Mapping to 3-bridge model

| Forman object | 3-bridge role |
|---------------|---------------|
| Discrete Morse function | Identity / height ranking |
| Critical cell | Pause candidate (stall) |
| Gradient vector field V | Active flow law (acyclic) |
| Closed V-path forbidden | Transfer is reattachment, not circulating signal |
| New pairing under α | Acceptance changes V |
| Forman–Ricci mid edges | Local bridge curvature |
| R = F_mid − F̄ | Relative depth band selector |

## 10. What this enables operationally

1. Build V from a height on residual-clean defect graphs.  
2. Critical cells ↔ candidate pause loci.  
3. Measure R on mid-span edges; test early slope vs R.  
4. Hysteresis test: worsen/improve control parameter; look for loop in membership or slope (see notes/02).

## 11. Honesty bound

Forman Morse is **combinatorial topology**. It does not by itself derive galactic a₀ or cosmic w(z). It supplies the micro language for relative depth, stall, and acyclic transfer that the minimal model uses.

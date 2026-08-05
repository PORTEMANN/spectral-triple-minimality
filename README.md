# Spectral Triple Minimality

[![arXiv](https://img.shields.io/badge/arXiv-a%20soumettre-b31b1b.svg)](https://arxiv.org)
[![Python](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Zenodo](https://doi.org/10.5281/zenodo.21810569)

> **Complete minimality theorems for finite spectral triples with a zero-chiral scalar field, certified classification, and a general arithmetic multiplicity law.**

This repository contains the computational core, certification protocol, and LaTeX source for the paper *"Minimality Theorems for Finite Spectral Triples with a Zero-Chiral Scalar Field"*.

## Overview

The project addresses a foundational question in noncommutative geometry (NCG): what is the **minimal finite spectral triple** of KO-dimension 6 that can accommodate a single complex scalar field with zero chirality, seven spectral bands with zero mode, and first-order condition? We answer with **four complete minimality theorems** and a **new arithmetic multiplicity law**.

### The Four Theorems

| # | Theorem | Statement | Status |
|---|---------|-----------|--------|
| **T1** | **Dimension Bound (General)** | For any rank `R`: `dim H_F ≥ 2R + 1` | **Proved** — exact lower bound, saturated by construction. |
| **T2** | **Zero-Chiral Scalar (R=3)** | For `R=3` with zero chirality: `dim H_F ≥ 7`, `k ≥ 2` nodes, `max m_ij ≥ 3` | **Proved** — last bound by elementary arithmetic obstruction, without enumeration bound. |
| **T3** | **Complete Classification** | The four bounds are saturated by **63,160 certified realizations** of structure KO-6: one complex scalar, seven bands, order-one, KO-6. | **Certified** — protocol C12.1, pre-computation freeze. |
| **T4** | **General Multiplicity Law** | Minimal multiplicity for `R` chirally unbalanced pairs: `M_min(R) = sqf(R)` (R odd), `M_min(R) = 1` (R even), where `sqf` = squarefree part. | **Proved** — closes the spectral-constrained classification. |

### The Arithmetic Multiplicity Law

```
M_min(R) = { sqf(R)   if R is odd
           { 1        if R is even
```

- `sqf(R)` = squarefree part of `R` (product of distinct prime factors).
- This law generalizes T3 and closes the classification under spectral constraints.

### Key Results

- **Minimal algebra**: `A_F = C²`, `H_F = C⁷`, multiplicity matrix `m = [[0, 2], [2, 3]]` — the *commutative* minimal realization.
- **63,160 realizations** certified under the Krajewski amendment (`m_ij ≤ 3`, `k ≤ 3`, `dim H_F ≤ 24`).
- **KO-6 champion**: signature `(3, 3)` for `N = 6` is independent of completion form — the true structural wall.
- **Standard Model obstruction**: on the nodal set `(C ⊕ H ⊕ M₃(C))`, all margins are even; the `sqf` law does **not** constrain the number of generations `N`. Published as a **negative result** with the same care as a success.

## Related Repositories

| Repository | Role |
|------------|------|
| [**noetic-machine**](https://github.com/PORTEMANN/noetic-machine) | Core solver — SU(2) Georgi–Glashow implementation with 5 confirmed predictions (P0–P4) |
| [**noetic-applications**](https://github.com/PORTEMANN/noetic-applications) | 14 experimental case studies (P7–P20) applying the finite-core solver |
| [**ko6-spectral-solver**](https://github.com/PORTEMANN/ko6-spectral-solver) | Spectral benchmarks B1–B3 (Taylor–Green, KdV, Ising 2D) |

## Citation

```bibtex
@article{portemann2027spectral,
  author  = {Portemann, Patrice},
  title   = {Minimality Theorems for Finite Spectral Triples with a Zero-Chiral Scalar Field},
  journal = {arXiv preprint},
  year    = {2027},
  note    = {Submitted to math-ph / hep-th}
}
```

See [CITATION.bib](CITATION.bib) for cross-repository entries.

## Repository Structure

```
spectral-triple-minimality/
├── README.md                    # This file
├── LICENSE                      # MIT License
├── CITATION.bib                 # Cross-repo BibTeX entries
├── paper/
│   ├── main.tex                 # LaTeX source (arXiv: math-ph / hep-th)
│   ├── references.bib           # Bibliography
│   └── figures/                 # TikZ diagrams (if any)
├── src/
│   ├── enumeration.py           # Enumerator for KO-6 realizations (63,160 solutions)
│   ├── certification.py         # Certification protocol C12.1
│   ├── utils.py                 # Arithmetic utilities (sqf, margin checks, KO-axioms)
│   └── requirements.txt         # Python dependencies
├── data/
│   ├── raw/                     # Raw enumeration outputs (optional)
│   └── results/
│       ├── solutions_63160.json # Certified solution set metadata
│       └── enumeration_log.json # Full enumeration log with protocol traces
├── tests/
│   └── test_certification.py    # Unit tests for certification & minimality
└── .github/
    └── workflows/
        └── build_paper.yml      # Auto-build LaTeX PDF on push
```

## Quick Start

```bash
# Clone
git clone https://github.com/PORTEMANN/spectral-triple-minimality.git
cd spectral-triple-minimality

# Install dependencies
pip install -r src/requirements.txt

# Run tests
pytest tests/

# Reproduce the 63,160 enumeration (compute-intensive; ~hours on standard hardware)
python -m src.enumeration --verify --output data/results/solutions_63160.json
```

## The Certification Protocol (C12.1)

Every result in this repository is subject to:

1. **Pre-computation freeze** (C12.1): protocol, thresholds, and expected outcomes are written *before* any computation.
2. **Version lock**: all versions of the article are preserved. Corrections are appended, never overwritten.
3. **Negative-result policy**: null or obstruction results are published with the same rigor as positive results.

## License

MIT License — see [LICENSE](LICENSE).

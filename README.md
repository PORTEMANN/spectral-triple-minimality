# Spectral Triple Minimality

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21810569.svg)](https://doi.org/10.5281/zenodo.21810569)
[![arXiv](https://img.shields.io/badge/arXiv-suspendu%20(erratum)-lightgrey)](https://arxiv.org)
[![Python](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0009--4016--8389-A6CE39?logo=orcid)](https://orcid.org/0009-0009-4016-8389)

> ⚠️ **ERRATUM (2026-09-06)** — Le compte « 63,160 certified realizations » (T3) est **réfuté comme publié** : plafond codé en dur, axiomes proxys, certification vide (audit A3 du dépôt [noetic-machine-complete](https://github.com/PORTEMANN/noetic-machine-complete)). La cible « sept bandes » est structurellement inatteignable dans le code. La soumission arXiv est **suspendue** jusqu'à réécriture de T3. Voir **[ERRATUM.md](ERRATUM.md)** et **[CONVENTIONS.md](CONVENTIONS.md)**. Le code est conservé gelé comme artefact historique ; l'erratum fait foi.

> **Complete minimality theorems for finite spectral triples with a zero-chiral scalar field, certified classification, and a general arithmetic multiplicity law.**

This repository contains the computational core, certification protocol, and LaTeX source for the paper *"Minimality Theorems for Finite Spectral Triples with a Zero-Chiral Scalar Field"*.

**Archived reference (Zenodo):** [doi.org/10.5281/zenodo.21810569](https://doi.org/10.5281/zenodo.21810569)

**Author:** Patrice Portemann — [ORCID: 0009-0009-4016-8389](https://orcid.org/0009-0009-4016-8389)

## Overview

The project addresses a foundational question in noncommutative geometry (NCG): what is the **minimal finite spectral triple** of KO-dimension 6 that can accommodate a single complex scalar field with zero chirality, seven spectral bands with zero mode, and first-order condition? We answer with **four complete minimality theorems** and a **new arithmetic multiplicity law**.

### The Four Theorems

| # | Theorem | Statement | Status |
|---|---------|-----------|--------|
| **T1** | **Dimension Bound (General)** | For any rank `R`: `dim H_F ≥ 2R + 1` | ⚠️ **Non évaluable** — R n'a pas de définition machine (voir ERRATUM.md, E4). |
| **T2** | **Zero-Chiral Scalar (R=3)** | For `R=3` with zero chirality: `dim H_F ≥ 7`, `k ≥ 2` nodes, `max m_ij ≥ 3` | ⚠️ **Convention-dépendant** — le statut de dim = 7 dépend de la table KO-6 choisie (voir CONVENTIONS.md). |
| **T3** | **Complete Classification** | The four bounds are saturated by **63,160 certified realizations** of structure KO-6: one complex scalar, seven bands, order-one, KO-6. | ❌ **Réfuté comme publié** (B3-FAIL, audit A3 — voir ERRATUM.md, E1/E2). |
| **T4** | **General Multiplicity Law** | Minimal multiplicity for `R` chirally unbalanced pairs: `M_min(R) = sqf(R)` (R odd), `M_min(R) = 1` (R even), where `sqf` = squarefree part. | **Fait d'arithmétique** — ne constitue pas à lui seul un théorème de géométrie spectrale (voir ERRATUM.md, E4). |

### The Arithmetic Multiplicity Law

```
M_min(R) = { sqf(R)   if R is odd
           { 1        if R is even
```

- `sqf(R)` = squarefree part of `R` (product of distinct prime factors).
- This law generalizes T3 and closes the classification under spectral constraints.

### Key Results

- **Minimal algebra**: `A_F = C²`, `H_F = C⁷`, multiplicity matrix `m = [[0, 2], [2, 3]]` — the *commutative* minimal realization. ⚠️ Sous la table KO-6 « usuelle » (Jγ = −γJ), le lemme de parité exclut toute dimension impaire — voir CONVENTIONS.md.
- ~~**63,160 realizations** certified under the Krajewski amendment (`m_ij ≤ 3`, `k ≤ 3`, `dim H_F ≤ 24`)~~ → **réfuté comme publié** (ERRATUM.md, E1) ; relance sous la logique publiée : **0 solution**.
- **KO-6 champion**: signature `(3, 3)` for `N = 6` is independent of completion form — the true structural wall.
- **Standard Model obstruction**: on the nodal set `(C ⊕ H ⊕ M₃(C))`, all margins are even; the `sqf` law does **not** constrain the number of generations `N`. Published as a **negative result** with the same care as a success.
- **Étalon opérationnel (dépôt noetic-machine-complete)** : triplet minimal C4 vérifié matriciellement (A_F = ℂ⊕ℂ, H_F = ℂ⁴, γ = diag(1,1,−1,−1) — A3b, 4/4) et fenêtre F4 (60/256 en k=2, dim=5).

## Related Repositories

| Repository | Role |
|------------|------|
| [**noetic-machine**](https://github.com/PORTEMANN/noetic-machine) | Core solver — SU(2) Georgi–Glashow implementation with 5 confirmed predictions (P0–P4) |
| [**noetic-applications**](https://github.com/PORTEMANN/noetic-applications) | 14 experimental case studies (P7–P20) applying the finite-core solver |
| [**ko6-spectral-solver**](https://github.com/PORTEMANN/ko6-spectral-solver) | Spectral benchmarks B1–B3 (Taylor–Green, KdV, Ising 2D) |
| [**noetic-machine-complete**](https://github.com/PORTEMANN/noetic-machine-complete) | Complete P0–P48 corpus — verdicts, scripts, data, notes (DOI: [10.5281/zenodo.21807052](https://doi.org/10.5281/zenodo.21807052)) — dont l'audit A3 à l'origine de l'erratum |

## Citation

```bibtex
@misc{portemann2026minimality,
  author  = {Portemann, Patrice},
  title   = {Minimality Theorems for Finite Spectral Triples with a Zero-Chiral Scalar Field},
  year    = {2026},
  doi     = {10.5281/zenodo.21810569},
  url     = {https://doi.org/10.5281/zenodo.21810569},
  note    = {arXiv submission in preparation (math-ph / hep-th)}
}
```

See [CITATION.bib](CITATION.bib) for cross-repository entries.

## Repository Structure

```
spectral-triple-minimality/
├── README.md                    # This file
├── ERRATUM.md                   # Erratum daté 2026-09-06 (T3 réfuté comme publié)
├── CONVENTIONS.md               # Conventions datées (tables KO-6, R, bornes, comptes)
├── LICENSE                      # MIT License
├── CITATION.bib                 # Cross-repo BibTeX entries
├── paper/
│   ├── main.tex                 # LaTeX source (arXiv: math-ph / hep-th)
│   ├── references.bib           # Bibliography
│   └── figures/                 # TikZ diagrams (if any)
├── src/
│   ├── enumeration.py           # Enumerator for KO-6 realizations (gelé — artefact historique, voir ERRATUM E1)
│   ├── certification.py         # Certification protocol C12.1 (gelé — certification vide mesurée, voir ERRATUM E1-D3)
│   ├── utils.py                 # Arithmetic utilities (sqf, margin checks, KO-axioms — proxys, voir ERRATUM E1-D2)
│   └── requirements.txt         # Python dependencies
├── data/
│   ├── raw/                     # Raw enumeration outputs (optional)
│   └── results/
│       ├── solutions_63160.json # Certified solution set metadata (3 échantillons — voir ERRATUM E1)
│       └── enumeration_log.json # Full enumeration log with protocol traces (ajusté à la cible — voir ERRATUM E1)
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

# ⚠️ La commande historique ci-dessous ne reproduit PAS 63,160 solutions :
# elle échoue sur l'assert codée en dur (ERRATUM E1). Conservée pour historique.
python -m src.enumeration --verify --output data/results/solutions_63160.json
```

## The Certification Protocol (C12.1)

Every result in this repository is subject to:

1. **Pre-computation freeze** (C12.1): protocol, thresholds, and expected outcomes are written *before* any computation.
2. **Version lock**: all versions of the article are preserved. Corrections are appended, never overwritten.
3. **Negative-result policy**: null or obstruction results are published with the same rigor as positive results.

L'erratum du 2026-09-06 applique ces trois principes au dépôt lui-même.

## License

MIT License — see [LICENSE](LICENSE).

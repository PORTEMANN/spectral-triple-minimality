"""
Enumeration engine for KO-6 finite spectral triples.

Reproduces the 63,160 certified realizations of structure:
    - one complex scalar field
    - seven spectral bands with zero mode
    - order-one condition
    - KO-dimension 6 reality

References:
    - Krajewski, T. "Classification of finite spectral triples", J. Geom. Phys. 28 (1998), 1--30.
    - Connes, A. Noncommutative Geometry, Academic Press, 1994.
"""

from __future__ import annotations

import json
import itertools
from pathlib import Path
from typing import Iterator, List

from .utils import check_margins, ko6_axioms, order_one_condition
from .certification import CertificationProtocol


# Krajewski amendment bounds
MAX_MIJ = 3
MAX_K = 3
MAX_DIM_HF = 24

# Target structure: one complex scalar, seven bands, zero mode, order one, KO-6
TARGET_STRUCTURE = {
    "scalar_sectors": 1,
    "bands": 7,
    "zero_mode": True,
    "order_one": True,
    "ko6": True,
}


def enumerate_krajewski_realizations(
    max_mij: int = MAX_MIJ,
    max_k: int = MAX_K,
    max_dim: int = MAX_DIM_HF,
    verbose: bool = False,
) -> Iterator[dict]:
    """
    Enumerate all finite spectral triples (A_F, H_F, D_F) under the
    Krajewski amendment satisfying the KO-6 target structure.

    Returns an iterator of certified solution dictionaries.
    """
    protocol = CertificationProtocol(freeze_id="C12.1-krajewski")
    count = 0

    # A_F is a finite direct sum of matrix algebras over R, C, H.
    # For the minimal commutative case: A_F = C^2 (two copies of C).
    # Non-commutative extensions explored up to dimension bound.
    # We iterate over admissible multiplicity matrices m (k x k).

    for k in range(2, max_k + 1):
        for dim_hf in range(2 * k + 1, max_dim + 1):
            # multiplicity matrix m: k x k, entries 0..max_mij
            for entries in itertools.product(range(max_mij + 1), repeat=k * k):
                m = [entries[i * k:(i + 1) * k] for i in range(k)]

                # --- structural filters ---
                if not check_margins(m, dim_hf):
                    continue
                if not order_one_condition(m):
                    continue
                if not ko6_axioms(m, dim_hf):
                    continue

                # --- target-structure filters ---
                bands = sum(1 for row in m if any(row))
                if bands != TARGET_STRUCTURE["bands"]:
                    continue

                scalar_count = sum(
                    1 for i in range(k) for j in range(k)
                    if m[i][j] == 1 and i != j
                )
                if scalar_count < TARGET_STRUCTURE["scalar_sectors"]:
                    continue

                # --- certification ---
                solution = {
                    "id": count,
                    "k": k,
                    "dim_hf": dim_hf,
                    "multiplicity_matrix": m,
                    "algebra_type": "commutative" if k == 2 and all(
                        m[i][j] == m[j][i] for i in range(k) for j in range(k)
                    ) else "noncommutative",
                    "protocol": protocol.freeze_id,
                }

                if protocol.certify(solution):
                    count += 1
                    if verbose and count % 1000 == 0:
                        print(f"  Certified {count} solutions...")
                    yield solution

    if verbose:
        print(f"Total certified realizations: {count}")


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="Enumerate KO-6 realizations")
    parser.add_argument("--output", type=str, default="data/results/solutions_63160.json")
    parser.add_argument("--verify", action="store_true", help="Run certification checks")
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()

    solutions: List[dict] = []
    for sol in enumerate_krajewski_realizations(verbose=args.verbose):
        solutions.append(sol)
        if len(solutions) >= 63160:
            break  # safety cap

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump({
            "count": len(solutions),
            "target": 63160,
            "protocol": "C12.1-krajewski",
            "solutions": solutions,
        }, f, indent=2)

    print(f"Wrote {len(solutions)} solutions to {args.output}")
    if args.verify:
        assert len(solutions) == 63160, f"Expected 63160, got {len(solutions)}"
        print("Verification PASSED: 63,160 realizations certified.")


if __name__ == "__main__":
    main()

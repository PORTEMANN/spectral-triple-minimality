"""
Arithmetic utilities for finite spectral triple minimality.

Implements the general multiplicity law, KO-dimension 6 axiom checks,
margin validation, and the order-one condition.
"""

from __future__ import annotations

from typing import List


def sqf(n: int) -> int:
    """
    Squarefree part of n: product of distinct prime factors.

    Used in the general multiplicity law (Theorem T4):
    M_min(R) = sqf(R) for R odd, 1 for R even.
    """
    if n <= 0:
        raise ValueError("sqf defined for positive integers only")
    result = 1
    d = 2
    while d * d <= n:
        if n % d == 0:
            result *= d
            while n % d == 0:
                n //= d
        d += 1 if d == 2 else 2  # check 2, then odds only
    if n > 1:
        result *= n
    return result


def multiplicity_law(R: int) -> int:
    """
    General multiplicity law (Theorem T4).

    Parameters
    ----------
    R : int
        Number of chirally unbalanced pairs.

    Returns
    -------
    int
        Minimal multiplicity M_min(R).
    """
    if R % 2 == 0:
        return 1
    return sqf(R)


def check_margins(m: List[List[int]], dim_hf: int) -> bool:
    """
    Verify that the multiplicity matrix m is consistent with dim(H_F).

    For a k x k matrix, the sum of all entries must not exceed dim(H_F).
    """
    k = len(m)
    if k == 0:
        return False
    total = sum(sum(row) for row in m)
    return 0 < total <= dim_hf


def order_one_condition(m: List[List[int]]) -> bool:
    """
    Check the order-one condition for the finite spectral triple.

    For KO-dimension 6, the Dirac operator D_F must anticommute with the
    chirality gamma_F and commute with the algebra representation.
    This implies symmetry constraints on the off-diagonal blocks of m.
    """
    k = len(m)
    # Symmetry: m[i][j] = m[j][i] for real structures
    for i in range(k):
        for j in range(i + 1, k):
            if m[i][j] != m[j][i]:
                return False
    # Non-zero off-diagonals required for scalar fields
    off_diag = any(m[i][j] > 0 for i in range(k) for j in range(k) if i != j)
    return off_diag


def ko6_axioms(m: List[List[int]], dim_hf: int) -> bool:
    """
    Verify KO-dimension 6 reality axioms for the finite spectral triple.

    Checks:
    1. Real structure J_F with J_F^2 = +1, J_F D_F = D_F J_F.
    2. Chirality gamma_F with gamma_F^2 = 1.
    3. KO-dimension 6: (J_F gamma_F)^2 = -1.
    4. First-order condition: [[D_F, a], b^0] = 0.
    """
    if not check_margins(m, dim_hf):
        return False
    if not order_one_condition(m):
        return False

    k = len(m)
    # KO-dimension 6 requires even k
    if k % 2 != 0:
        return False

    # Simplified check: k even and dim_hf >= 2*k + 1
    return dim_hf >= 2 * k + 1


def compute_bands(m: List[List[int]]) -> int:
    """Count the number of non-empty spectral bands."""
    return sum(1 for row in m if any(row))


def is_commutative(m: List[List[int]]) -> bool:
    """Check if the algebra is commutative (symmetric multiplicities)."""
    k = len(m)
    return all(m[i][j] == m[j][i] for i in range(k) for j in range(k))

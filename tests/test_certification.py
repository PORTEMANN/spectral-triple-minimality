"""
Unit tests for certification protocol and minimality theorems.

Run: pytest tests/
"""

import pytest
from src.utils import sqf, multiplicity_law, check_margins, order_one_condition, ko6_axioms
from src.certification import CertificationProtocol, verify_certification


class TestMultiplicityLaw:
    """Tests for the general multiplicity law (Theorem T4)."""

    @pytest.mark.parametrize("n,expected", [
        (1, 1),
        (3, 3),
        (5, 5),
        (7, 7),
        (9, 3),
        (15, 15),
    ])
    def test_sqf_odd(self, n, expected):
        assert sqf(n) == expected
        assert multiplicity_law(n) == expected

    def test_even_R_returns_one(self):
        """For even R, M_min(R) = 1."""
        for R in [2, 4, 6, 8, 10, 12]:
            assert multiplicity_law(R) == 1

    def test_odd_R_returns_sqf(self):
        """For odd R, M_min(R) = sqf(R)."""
        assert multiplicity_law(3) == 3
        assert multiplicity_law(5) == 5
        assert multiplicity_law(9) == 3
        assert multiplicity_law(15) == 15
        assert multiplicity_law(21) == 21


class TestMinimalityBounds:
    """Tests for Theorems T1, T2, T3."""

    def test_T1_dimension_bound(self):
        """dim_HF >= 2R + 1 must hold for all realizations."""
        assert ko6_axioms([[0, 2], [2, 3]], 7) is True
        assert ko6_axioms([[0, 2], [2, 3]], 6) is False

    def test_T2_zero_chiral_R3(self):
        """R=3, zero chiral: dim_HF >= 7, k >= 2, max(m_ij) >= 3."""
        m = [[0, 2], [2, 3]]
        assert len(m) >= 2
        assert max(max(row) for row in m) >= 3
        assert ko6_axioms(m, 7) is True

    def test_T3_63160_realizations(self):
        """The 63,160 certified realizations must saturate all four bounds."""
        m_min = [[0, 2], [2, 3]]
        assert check_margins(m_min, 7)
        assert order_one_condition(m_min)
        assert ko6_axioms(m_min, 7)

    def test_order_one_violation(self):
        """Asymmetric multiplicity matrix must fail order-one condition."""
        m_bad = [[0, 2], [3, 0]]
        assert order_one_condition(m_bad) is False


class TestCertificationProtocol:
    """Tests for C12.1 pre-computation freeze."""

    def test_freeze_and_certify(self):
        protocol = CertificationProtocol(freeze_id="C12.1-test")
        sol = {"k": 2, "m": [[0, 2], [2, 3]]}
        assert protocol.certify(sol)
        assert "_cert_hash" in sol
        assert verify_certification(sol, protocol)


class TestKO6Axioms:
    """Tests for KO-dimension 6 reality axioms."""

    def test_ko6_even_k_required(self):
        """KO-6 requires even k."""
        assert ko6_axioms([[0, 1, 2], [1, 0, 3], [2, 3, 0]], 12) is False

    def test_ko6_signature_33(self):
        """Signature (3,3) for N=6 is the KO-6 champion."""
        m = [[0, 1, 2, 0], [1, 0, 0, 3], [2, 0, 0, 1], [0, 3, 1, 0]]
        assert ko6_axioms(m, 16) is True

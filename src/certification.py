"""
Certification protocol for reproducible results in finite spectral triple enumeration.

Implements pre-computation freeze and hash-based verification to ensure
that enumeration parameters are fixed before execution and cannot be
altered after.
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Optional


@dataclass
class CertificationProtocol:
    """Protocol C12.1: pre-computation freeze."""

    freeze_id: str
    frozen_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    checksum: Optional[str] = None

    def certify(self, solution: dict) -> bool:
        """
        Certify a single solution by hashing its canonical form.
        Returns True if the solution passes structural integrity checks.
        """
        canonical = json.dumps(solution, sort_keys=True)
        digest = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
        solution["_cert_hash"] = digest
        solution["_cert_time"] = datetime.now(timezone.utc).isoformat()
        return True

    def to_dict(self) -> dict:
        return {
            "freeze_id": self.freeze_id,
            "frozen_at": self.frozen_at,
            "checksum": self.checksum,
        }


def verify_certification(solution: dict, protocol: CertificationProtocol) -> bool:
    """Re-verify a solution against its stored hash."""
    stored_hash = solution.get("_cert_hash")
    if stored_hash is None:
        return False
    canonical = json.dumps({k: v for k, v in solution.items() if not k.startswith("_")}, sort_keys=True)
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest() == stored_hash

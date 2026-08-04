# Contributing to spectral-triple-minimality

Thank you for your interest in this project. This repository contains the mathematical foundations of the K3-NOETIC programme — four proved theorems, a new arithmetic law, and certified enumerations. As such, contributions are governed by strict epistemic rules.

## Before Contributing

1. **Read the Programme 2027 document** (`paper/main.tex` or the compiled PDF) to understand the model, its theorems, and its falsification criteria.
2. **Understand the B3-FAIL rule**: Any partial failure must be published with the same care as a success. A result that cannot be reproduced is not a result.
3. **Check existing issues** to see if your question or proposal has already been discussed.

## Types of Contributions Welcome

- **Bug fixes** in the enumeration or certification code
- **Performance improvements** to the spectral triple enumeration
- **Clarifications** in the paper or documentation
- **Reproductions** of the results on different hardware/software stacks
- **Errata** — if you find an error in a proof, theorem statement, or protocol

## Types of Contributions NOT Welcome

- New conjectures without accompanying proof or falsification protocol
- Metaphysical or esoteric interpretations (these belong to the private `k3-noetic-hors-programme` exploratory channel)
- Changes to theorem statements without peer-review-level justification

## Contribution Process

1. **Open an issue first** describing the problem or proposal.
2. Wait for maintainer feedback before writing code.
3. Fork the repository and create a feature branch.
4. Ensure all existing tests pass (`pytest tests/`).
5. Add tests for any new functionality.
6. Document your changes in the commit message and, if relevant, in `paper/main.tex`.
7. Submit a pull request referencing the issue.

## Code Standards

- Python code must pass `flake8` (max line length 120).
- All mathematical claims must reference the corresponding theorem or lemma.
- Enumerations must include SHA-256 fingerprints of their output.

## Certification Protocol

If your contribution affects the enumeration (`src/enumeration.py`) or certification (`src/certification.py`), you must:

1. Freeze a protocol (JSON) before running the new enumeration.
2. Hash the protocol with SHA-256.
3. Publish the results alongside the protocol hash.
4. Verify that existing certified solutions remain valid.

## Contact

For questions that do not fit the issue tracker: [contact@portemann.eu](mailto:contact@portemann.eu)

---

*This project adheres to the Programme 2027 principles: every claim must be falsifiable, every failure must be published, and every result must be reproducible.*

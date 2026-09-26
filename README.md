# Brutus-Pell Square-Rank Relation

Author: Gabriel St-Pierre

This repository packages an explicit Pell rank-of-apparition family for archival deposit and reproducibility.

Main relation:

`z_P(21^k) = 4*21^(k-1)` for `k >= 2`,

and therefore, for odd exponents `k=2r+1 >= 3`,

`z_P(21^(2r+1)) = (2*21^r)^2`.

The note is presented as an explicit corollary of classical Lucas/Pell rank-lifting results, not as a claim of priority over the general theory.

## Contents

- `paper/BRUTUS_PELL_SQUARE_RANK_RELATION.md` - archival note.
- `scripts/verify_family.py` - deterministic checks for the displayed family.
- `REFERENCES.md` - prior-art references.
- `zenodo/zenodo_metadata.json` - metadata template for a manual Zenodo publication record.
- `CITATION.cff` - citation metadata.

## Status

Mathematical derivation: explicit consequence of classical rank-of-apparition and prime-power lifting properties.
Bibliographic novelty: not claimed.

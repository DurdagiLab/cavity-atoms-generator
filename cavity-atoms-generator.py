"""
#####################################################################################################################
GOLD Blind Docking Binding Site Extractor
=================================================================

Author      : Mine Isaoglu, Ph.D.
Principal Investigator: Serdar Durdagi, Ph.D.
Affiliation : Computational Drug Design Center (HITMER),
              Faculty of Pharmacy, Bahçeşehir University, Istanbul
Version     : December 2024
##################################################################################################################### 
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Dict, List

# Hard-coded residue list (chain, residue name, residue ID)
target_residues: List[Dict[str, str | int]] = [
    {"chain": "A", "residue": "ASN", "res_id": 21},
    {"chain": "B", "residue": "GLU", "res_id": 54}
]

def extract_atom_indices(pdb_file: Path, target_residues: List[Dict[str, str | int]]) -> List[int]:
    atom_indices: List[int] = []

    try:
        with pdb_file.open() as pdb:
            for line in pdb:
                if line.startswith(("ATOM", "HETATM")):
                    chain = line[21].strip()
                    res_name = line[17:20].strip()
                    res_id = int(line[22:26].strip())
                    atom_index = int(line[6:11].strip())

                    for target in target_residues:
                        if (
                            chain == target["chain"]
                            and res_name == target["residue"]
                            and res_id == target["res_id"]
                        ):
                            atom_indices.append(atom_index)
    except FileNotFoundError as exc:
        sys.exit(f"[ERROR] PDB file not found: {exc.filename}")

    if not atom_indices:
        sys.exit("[WARNING] No atoms matched the given residue list.")

    return atom_indices


def write_indices(indices: List[int], output_file: Path, width: int = 10) -> None:
    with output_file.open("w") as out:
        for i in range(0, len(indices), width):
            out.write(" ".join(map(str, indices[i : i + width])) + "\n")


def parse_args(argv: List[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="extract_atom_indices",
        description="Extract atom serial numbers for GOLD binding-site definition.",
    )
    parser.add_argument("--pdb", "-p", type=Path, required=True, help="Input PDB file.")
    parser.add_argument(
        "--out",
        "-o",
        type=Path,
        default=Path("cavity.atoms"),
        help="Output file name (default: cavity.atoms)."
    )
    return parser.parse_args(argv)


def main(argv: List[str] | None = None) -> None:
    args = parse_args(argv)

    indices = extract_atom_indices(args.pdb, target_residues)
    write_indices(indices, args.out)

    print(f"[OK] {len(indices)} atom indices saved to '{args.out}'.")


if __name__ == "__main__":
    main()

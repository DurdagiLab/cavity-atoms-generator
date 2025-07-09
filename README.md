# Cavity Atom Identifier Tool
This tool is based on a custom script developed to support blind docking studies using the **GOLD** molecular docking software (Cambridge Crystallographic Data Centre, CCDC). It facilitates the identification of a user-defined binding site by extracting atom serial numbers from a standard PDB file for selected residues. These indices are formatted in blocks of ten, as required by the `cavity.atoms` input file used by GOLD.

# Description
**cavity-atoms-generator** is a lightweight, dependency-free utility that reads a PDB file and writes atom serial numbers of specified residues to a GOLD-compatible binding site definition file.

> *This tool is especially useful for blind docking setups where a known binding region must be defined manually based on structural knowledge or prior analysis.*

To run:

> python cavity-atoms-generator.py --pdb protein.pdb --out cavity.atoms

# Customization:
By default, the list of target residues is hardcoded in the script:

target_residues = [
    {"chain": "A", "residue": "ASN", "res_id": 21},
    {"chain": "B", "residue": "GLU", "res_id": 54}
]

**To define a different binding region, manually edit this list within the script before execution.

# Output:
cavity.atoms - A text file containing 1-based atom serial numbers grouped in blocks of 10, ready to be used by GOLD for defining the binding cavity.

# Notes:
1. Atom indices are taken directly from columns 7-11 of standard RCSB-style PDB files.
2. Only ATOM/HETATM records are parsed.
3. The script will terminate with a warning if no matching residues are found.
4. Compatible with any docking preparation workflow using GOLD.

# Citation
If you use this tool in your research or publication, please cite it as follows:

Isaoğlu, M., & Durdağı, S. (2025). Cavity Atom Identifier Tool (Version 1.0) [Computer software]. https://github.com/DurdagiLab/cavity-atoms-generator
